# Generated by Django 3.1 on 2020-08-12 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20200809_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='language',
        ),
    ]
