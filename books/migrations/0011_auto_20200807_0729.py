# Generated by Django 3.1 on 2020-08-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20200806_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('statistics_global', 'Can see global statistics'), ('statistics_user', 'Can see user statistics'))},
        ),
    ]