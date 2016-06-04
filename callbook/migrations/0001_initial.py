# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=500)),
                ('cnt', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
