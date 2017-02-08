# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "news_category"
        verbose_name = "Категория новостей"
        verbose_name_plural = "news_category"

    name = models.CharField(max_length=50, verbose_name="Имя категорий")


class News(models.Model):
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "news"
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    title = models.CharField(max_length=50, verbose_name="Новости")
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name="Выбирите категорию")
    image = models.ImageField()
    tags = models.CharField(max_length=50)
    description_short = models.TextField(max_length=250)
    description_full = RichTextField()
    date_posting = models.DateTimeField(default=timezone.now)
    date_editing = models.DateTimeField(default=timezone.now)
    published = models.BooleanField()
    author = models.ForeignKey(User, null=True, blank=True)
