# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-18 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20190518_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]