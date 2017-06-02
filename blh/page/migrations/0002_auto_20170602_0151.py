# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='heading',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
