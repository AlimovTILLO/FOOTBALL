# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0014_auto_20170207_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='season',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='football.Season'),
        ),
    ]