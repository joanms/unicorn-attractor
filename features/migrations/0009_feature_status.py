# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-15 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_auto_20190514_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='status',
            field=models.TextField(default='To do'),
        ),
    ]