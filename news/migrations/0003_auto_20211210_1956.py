# Generated by Django 3.2.9 on 2021-12-10 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
