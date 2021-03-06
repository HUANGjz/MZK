# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callbook', '0007_tagname'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('if_second', models.BooleanField()),
                ('if_event', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='EventCatalog',
        ),
        migrations.DeleteModel(
            name='SingerCatalog',
        ),
        migrations.DeleteModel(
            name='TagName',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_name',
        ),
        migrations.AddField(
            model_name='tag',
            name='callbook',
            field=models.ManyToManyField(to='callbook.CallBook'),
        ),
        migrations.AlterField(
            model_name='picpath',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callbook.CallBook'),
        ),
        migrations.AlterField(
            model_name='secondcatalog',
            name='firstcatalog_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callbook.FirstCatalog'),
        ),
        migrations.AlterField(
            model_name='secondcatalog',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callbook.Tag'),
        ),
        migrations.AddField(
            model_name='firstcatalog',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callbook.Tag'),
        ),
    ]
