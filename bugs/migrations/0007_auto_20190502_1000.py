# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 09:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0006_bug_upvoters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='upvoters',
        ),
        migrations.AddField(
            model_name='bug',
            name='upvoters',
            field=models.ManyToManyField(related_name='_bug_upvoters_+', to=settings.AUTH_USER_MODEL),
        ),
    ]