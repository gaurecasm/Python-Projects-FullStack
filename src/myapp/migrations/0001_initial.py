# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-01-02 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=45.54, max_digits=20)),
            ],
        ),
    ]
