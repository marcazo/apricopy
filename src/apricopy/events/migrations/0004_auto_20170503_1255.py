# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170503_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]