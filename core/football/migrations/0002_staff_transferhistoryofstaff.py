# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('date_born', models.DateTimeField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('image', models.ImageField(upload_to=b'')),
                ('license_type', models.CharField(choices=[('PRO', 'PRO'), ('\u0410', '\u0410'), ('\u0412', '\u0412')], max_length=10)),
                ('license_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'staff',
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='TransferHistoryOfStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Teams')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Staff')),
            ],
            options={
                'db_table': 'transfer_history_of_staff',
                'verbose_name': 'Transfer History Of Staff',
                'verbose_name_plural': 'Transfer History Of Staff',
            },
        ),
    ]
