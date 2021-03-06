# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_title', models.CharField(max_length=250)),
                ('audio_length', models.CharField(max_length=250)),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=250)),
                ('video_logo', models.CharField(max_length=250)),
                ('length', models.IntegerField()),
            ],
        ),
    ]
