# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-18 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20190518_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=999),
        ),
    ]