# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from smart_selects.db_fields import ChainedManyToManyField
from __builtin__ import unicode
from django.utils import timezone
from django.db import models


# Create your models here.
class Teams(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "teams"
        verbose_name = "Teams"
        verbose_name_plural = "Teams"

    name = models.CharField(max_length=50)
    logo = models.ImageField()
    founded = models.DateTimeField(default=timezone.now)
    website = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    vk = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)


class Championship(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "championship"
        verbose_name = "Championship"
        verbose_name_plural = "Championship"

    name = models.CharField(max_length=50)


class Season(models.Model):
    def __unicode__(self):
        return unicode(self.beginning_of_the_season) or u''

    class Meta:
        db_table = "season"
        verbose_name = "Season"
        verbose_name_plural = "Season"

    championships = models.ForeignKey(Championship)
    beginning_of_the_season = models.DateTimeField(default=timezone.now)
    end_of_season = models.DateTimeField(default=timezone.now)
    club_members = models.ManyToManyField(Teams)
