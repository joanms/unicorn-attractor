# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0015_auto_20190516_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featureupvote',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='featureupvote',
            name='user',
        ),
        migrations.DeleteModel(
            name='FeatureUpvote',
        ),
    ]
