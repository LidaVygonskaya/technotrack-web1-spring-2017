# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 23:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_post_likecount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likecount',
        ),
    ]
