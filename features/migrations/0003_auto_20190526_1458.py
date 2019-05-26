# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-26 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20190521_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('In progress', 'In progress'), ('Done', 'Done')], default='To do', max_length=20),
        ),
    ]
