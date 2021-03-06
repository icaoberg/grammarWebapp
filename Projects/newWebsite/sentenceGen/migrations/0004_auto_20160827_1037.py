# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentenceGen', '0003_auto_20160827_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('score', models.IntegerField(default=0)),
                ('mode', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='PostAd',
        ),
    ]
