# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_auto_20160606_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='axis_data',
            name='z',
            field=models.IntegerField(default=0),
        ),
    ]