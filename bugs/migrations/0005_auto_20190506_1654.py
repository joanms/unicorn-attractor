# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_auto_20190506_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bug',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bugs.Bug'),
        ),
    ]
