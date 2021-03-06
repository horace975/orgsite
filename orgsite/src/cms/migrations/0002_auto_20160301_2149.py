# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 13:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutblock',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 1, 13, 48, 32, 217839, tzinfo=utc), verbose_name='About DateTime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioblock',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 1, 13, 48, 43, 611897, tzinfo=utc), verbose_name='Portfolio DateTime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicesblock',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 1, 13, 49, 11, 638018, tzinfo=utc), verbose_name='Services DateTime'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolioblock',
            name='tag',
            field=models.CharField(max_length=30, verbose_name='Portfolio tag'),
        ),
        migrations.AlterField(
            model_name='portfolioblock',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Portfolio name'),
        ),
    ]
