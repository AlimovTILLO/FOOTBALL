# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from django.db import models


# Create your models here.
class VideoCategory(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "video_category"
        verbose_name = "Категория видео"
        verbose_name_plural = "Video Category"

    name = models.CharField(max_length=50, verbose_name="Имя категорий")


class Videos(models.Model):
    def __unicode__(self):
        return self.description_short

    class Meta:
        db_table = "videos"
        verbose_name = "Videos"
        verbose_name_plural = "Videos"

    link = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    category = models.ForeignKey(VideoCategory)
    description_short = models.TextField()
    date_posting = models.DateTimeField()
    date_editing = models.DateTimeField(default=timezone.now)
    published = models.BooleanField()
    author = models.CharField(max_length=50)

