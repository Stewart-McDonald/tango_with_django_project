# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-06 20:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_category_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='dislikes',
        ),
    ]
