# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamsgroup', '0002_events_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='category',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
