# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamsgroup', '0008_auto_20160823_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='college',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
