# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 20:21
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_content2'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
