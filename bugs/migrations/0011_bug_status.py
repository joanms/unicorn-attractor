# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0010_remove_bug_upvoters'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='status',
            field=models.TextField(default='To do'),
        ),
    ]
