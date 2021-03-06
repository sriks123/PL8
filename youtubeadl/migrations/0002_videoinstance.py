# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeadl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique id for the this video across the videoLibrary', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('d', 'downloaded'), ('n', 'not Downloaded')], default='n', help_text='video avaibility', max_length=1)),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='youtubeadl.Video')),
            ],
        ),
    ]
