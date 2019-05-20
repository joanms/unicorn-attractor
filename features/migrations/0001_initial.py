# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-20 15:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('upvotes', models.IntegerField(default=0)),
                ('amount_paid', models.IntegerField(default=0)),
                ('status', models.TextField(default='To do')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_commenter', to=settings.AUTH_USER_MODEL)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.Feature')),
            ],
        ),
    ]
