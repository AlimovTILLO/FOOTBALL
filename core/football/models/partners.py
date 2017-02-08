# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class PartnersBanner(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "partners_banner"
        verbose_name = "Partners Banner"
        verbose_name_plural = "Partners Banner"

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    logo = models.ImageField()

