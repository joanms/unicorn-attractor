# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-14 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_comment_upvote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='FeatureComment',
        ),
        migrations.RenameModel(
            old_name='Upvote',
            new_name='FeatureUpvote',
        ),
    ]
