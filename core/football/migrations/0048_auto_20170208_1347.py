# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0047_auto_20170208_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='book',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='publications',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
    ]
