# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 08:38
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0059_auto_20170208_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='guests',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='championship', chained_model_field='club_members', on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='football.Teams'),
        ),
        migrations.AlterField(
            model_name='match',
            name='season',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='championship', chained_model_field='championships', on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='football.Season'),
        ),
    ]
