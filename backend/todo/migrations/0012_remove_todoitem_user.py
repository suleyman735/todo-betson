# Generated by Django 4.2.5 on 2023-11-24 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_user_alter_todoitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]
