# Generated by Django 4.2.5 on 2023-10-19 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_todoitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]
