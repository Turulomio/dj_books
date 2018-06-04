# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-04 20:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180225_0614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valoration',
            options={'managed': True, 'ordering': ['valoration', 'read_end', 'read_start']},
        ),
        migrations.AlterField(
            model_name='author',
            name='birth',
            field=models.IntegerField(blank=True, null=True, verbose_name='Birth year'),
        ),
        migrations.AlterField(
            model_name='author',
            name='death',
            field=models.IntegerField(blank=True, null=True, verbose_name='Death year'),
        ),
        migrations.AlterField(
            model_name='author',
            name='family_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Family name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Birth date'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('ES', 'Español'), ('EN', 'English'), ('FR', 'Francés')], default='EN', max_length=2, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='valoration',
            name='read_end',
            field=models.DateField(blank=True, null=True, verbose_name='Date read ended'),
        ),
        migrations.AlterField(
            model_name='valoration',
            name='read_start',
            field=models.DateField(blank=True, null=True, verbose_name='Date read started'),
        ),
        migrations.AlterField(
            model_name='valoration',
            name='valoration',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Valoration [0-100]'),
        ),
    ]
