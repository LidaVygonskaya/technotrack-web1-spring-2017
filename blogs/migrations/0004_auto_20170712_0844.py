# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 08:44
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_post_likecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
