# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0017_auto_20170207_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='season',
            field=models.ManyToManyField(to='football.Season'),
        ),
    ]