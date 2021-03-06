# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 07:27
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0042_auto_20170208_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='championship',
            field=smart_selects.db_fields.ChainedForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Championship'),
        ),
    ]
