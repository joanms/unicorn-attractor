# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 09:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0002_auto_20190521_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugupvote',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
