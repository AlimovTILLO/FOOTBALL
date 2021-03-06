# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 07:42
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0045_auto_20170208_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='championship',
        ),
        migrations.AddField(
            model_name='season',
            name='championship',
            field=smart_selects.db_fields.ChainedForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='football.Championship'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='season',
            name='club_members',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, to='football.Teams'),
        ),
    ]
