# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('animeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='anime_studio',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
