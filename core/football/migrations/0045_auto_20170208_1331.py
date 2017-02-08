# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0044_auto_20170208_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('publications', models.ManyToManyField(blank=True, null=True, to='football.Publication')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Publication'),
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='publication', chained_model_field='publications', on_delete=django.db.models.deletion.CASCADE, to='football.Writer'),
        ),
    ]
