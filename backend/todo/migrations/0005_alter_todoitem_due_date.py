# Generated by Django 4.2.5 on 2023-10-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todoitem_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(verbose_name='Will Finish'),
        ),
    ]