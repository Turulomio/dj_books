# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-05 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180604_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(null=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='valoration',
            name='book',
            field=models.ForeignKey(db_column='id_books', on_delete=django.db.models.deletion.DO_NOTHING, to='books.Book', verbose_name='Book'),
        ),
    ]
