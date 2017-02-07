# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class About(models.Model):
    class Meta:
        db_table = "about"
        verbose_name = "About"
        verbose_name_plural = "About"

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)

    def __unicode__(self):
        return self.title
