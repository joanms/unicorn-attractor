# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 11:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0007_auto_20190502_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='upvoters',
            field=models.ManyToManyField(blank=True, related_name='users_upvoters', to=settings.AUTH_USER_MODEL),
        ),
    ]
