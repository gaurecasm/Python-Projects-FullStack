# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-01-02 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=myapp.models.file_modi),
        ),
    ]