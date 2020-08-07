# Generated by Django 3.1 on 2020-08-07 08:05

from django.db import migrations

def apply_migration(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Group = apps.get_model('auth', 'Group')
    Group.objects.bulk_create([
        Group(name='Default library workers'),
        Group(name='Default library users'),
    ])

def revert_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(
        name__in=[
            Group(name='Default library workers'),
            Group(name='Default library users'),
        ]
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20200807_0729'),
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration),
    ]