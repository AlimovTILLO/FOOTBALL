# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 10:13
from __future__ import unicode_literals

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0083_auto_20170208_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='club_members',
            field=smart_selects.db_fields.ChainedManyToManyField(to='football.Teams'),
        ),
    ]
