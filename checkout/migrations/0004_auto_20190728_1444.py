# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-28 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20190521_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]