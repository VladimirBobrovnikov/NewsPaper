from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def notify_managers_posts(sender, instance, created, **kwargs):
    html_content = render_to_string(
        'new/post_changes_create.html',
        {'post': instance, }
    )
    recipients = [user.get('email') for user in instance.category.subscribed_users]
    if created:
        start_word = 'Новая'
    else:
        start_word = 'Обновлена'
    msg = EmailMultiAlternatives(
        subject=f'{start_word} статья на сайте: {instance.title}',
        body=f'На сайте NewsPaper {start_word.lower()} статья:{instance.title}, {instance.preview()}',
        to=recipients
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
