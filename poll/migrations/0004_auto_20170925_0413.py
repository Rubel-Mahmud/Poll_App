# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20170925_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date Published'),
        ),
    ]
