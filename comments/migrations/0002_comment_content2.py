# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 19:03
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content2',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
