# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamsgroup', '0005_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='collegeName',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='userName',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
