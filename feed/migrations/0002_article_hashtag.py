# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-27 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hashtag',
            field=models.ManyToManyField(to='feed.HashTag'),
        ),
    ]
