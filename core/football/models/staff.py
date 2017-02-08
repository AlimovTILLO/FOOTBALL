# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django_countries.fields import CountryField
# from .team import Teams


# Create your models here.
class Staff(models.Model):
    class Meta:
        db_table = "staff"
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    LICENSE_CHOICES = (
        ('PRO', 'PRO'),
        ('А', 'А'),
        ('В', 'В'),
    )

    full_name = models.CharField(max_length=50)
    date_born = models.DateTimeField()
    country = CountryField(blank_label='(select country)')
    image = models.ImageField()
    license_type = models.CharField(max_length=10, choices=LICENSE_CHOICES)
    license_date = models.DateTimeField()

    def __unicode__(self):
        return self.full_name


# class TransferHistoryOfStaff(models.Model):
#     class Meta:
#         db_table = "transfer_history_of_staff"
#         verbose_name = "Transfer History Of Staff"
#         verbose_name_plural = "Transfer History Of Staff"
#
#     staff = models.ForeignKey(Staff)
#     command = models.ForeignKey(Teams)
#     composition = models.CharField(max_length=50)
#     position = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.staff
