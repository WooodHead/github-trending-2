# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todaytrend',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
