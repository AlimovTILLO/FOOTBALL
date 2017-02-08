# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 10:45
from __future__ import unicode_literals

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0087_auto_20170208_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='members',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='season', to='football.Teams'),
        ),
    ]