# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbook', '0002_callbook_singer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='callbook',
            name='file_path',
        ),
    ]
