# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0003_auto_20160224_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemessage',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='E-mail'),
        ),
    ]
