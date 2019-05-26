# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-26 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0005_auto_20190526_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('In progress', 'In progress'), ('Done', 'Done')], default='To do', max_length=2),
        ),
    ]
