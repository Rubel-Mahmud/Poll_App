# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 23:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 23, 15, 3, 250448, tzinfo=utc)),
        ),
    ]
