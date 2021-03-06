# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(max_length=30, verbose_name='About Pic')),
                ('title', models.CharField(max_length=30, verbose_name='About Title')),
                ('content', models.CharField(max_length=100, verbose_name='About Content')),
            ],
        ),
        migrations.CreateModel(
            name='HomeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Main Title')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Sub Title')),
            ],
        ),
        migrations.CreateModel(
            name='MainBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=30, verbose_name='Shop Name')),
                ('services', models.CharField(max_length=30, verbose_name='Our Services')),
                ('portfolio', models.CharField(max_length=30, verbose_name='Our Portfolio')),
                ('aboutus', models.CharField(max_length=30, verbose_name='About Us')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Project name')),
                ('tag', models.CharField(max_length=30, verbose_name='Project tag')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(max_length=30, verbose_name='Services Pic')),
                ('title', models.CharField(max_length=30, verbose_name='Services Title')),
                ('content', models.CharField(max_length=100, verbose_name='Services Content')),
            ],
        ),
    ]
