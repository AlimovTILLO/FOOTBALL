# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Publication(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(max_length=255)
    publications = models.ManyToManyField('Publication', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    publication = models.ForeignKey(Publication)
    writer = ChainedForeignKey(
        Writer,
        chained_field="publication",
        chained_model_field="publications",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

