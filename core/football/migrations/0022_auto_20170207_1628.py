# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0021_auto_20170207_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='season',
            field=models.ManyToManyField(related_name='_match_season_+', to='football.Season'),
        ),
    ]
