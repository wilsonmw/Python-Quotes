# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 23:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0003_auto_20170728_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='content',
        ),
    ]