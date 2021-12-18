from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.conf import settings
from .models import Post

@receiver(post_save, sender=Post)
def notify_managers_posts(sender, instance, created, **kwargs):

    html_content = render_to_string(
        'news/post_changes_create.html',
        {'post': instance, }
    )
    for category in instance.category.all():
        recipients = [user.email for user in category.subscribed_users.all()]
        if created:
            start_word = 'Новая'
        else:
            start_word = 'Обновлена'
        msg = EmailMultiAlternatives(
            subject=f'На сайте NewsPaper {start_word.lower()} статья: {instance.title}',
            body=f'На сайте NewsPaper {start_word.lower()} статья: {instance.title}',
            from_email=settings.SERVER_EMAIL,
            to=recipients
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
