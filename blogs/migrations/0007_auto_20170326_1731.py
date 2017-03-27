# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 17:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20170326_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='owner',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
