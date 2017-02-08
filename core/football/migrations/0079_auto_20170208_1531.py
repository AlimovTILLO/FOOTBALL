# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0078_auto_20170208_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='teams',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='football.Teams'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='guests',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='season', chained_model_field='teams', on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='football.Teams'),
        ),
        migrations.AlterField(
            model_name='match',
            name='host',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='season', chained_model_field='teams', on_delete=django.db.models.deletion.CASCADE, related_name='host', to='football.Teams'),
        ),
    ]
