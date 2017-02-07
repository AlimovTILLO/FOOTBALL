# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __builtin__ import unicode
from django.utils import timezone

from django.db import models
from django_countries.fields import CountryField
from .team import Teams, Championship, Season


# Create your models here.
class Players(models.Model):
    def __unicode__(self):
        return self.full_name

    class Meta:
        db_table = "players"
        verbose_name = "Players"
        verbose_name_plural = "Players"

    image = models.ImageField()
    full_name = models.CharField(max_length=50)
    date_born = models.DateTimeField(default=timezone.now)
    country = CountryField(blank_label='(select country)')
    growth = models.DecimalField(max_digits=5, decimal_places=2)
    heft = models.DecimalField(max_digits=5, decimal_places=2)


class ClubPlayers(models.Model):
    def __unicode__(self):
        return unicode(self.player) or u''

    class Meta:
        db_table = "club_players"
        verbose_name = "Club Players"
        verbose_name_plural = "Club Players"

    POSITION_CHOICES = (
        ('Вратарь', 'Вратарь'),
        ('Защитник', 'Защитник'),
        ('Полузащитник', 'Полузащитник'),
        ('Нападающий', 'Нападающий'),
    )
    player = models.ForeignKey(Players)
    club = models.ForeignKey(Teams)
    image = models.ImageField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    number = models.IntegerField()
    start_a_career_in_this_club = models.DateTimeField(default=timezone.now)
    end_of_a_career_in_this_club = models.DateTimeField(default=timezone.now)


class Match(models.Model):
    def __unicode__(self):
        return unicode(self.date_of_the_match) or u''

    class Meta:
        db_table = "match"
        verbose_name = "Match"
        verbose_name_plural = "Match"

    championship = models.ForeignKey(Championship)
    season = models.ForeignKey(Season)
    tour = models.IntegerField()
    host = models.CharField(max_length=50)
    guests = models.CharField(max_length=50)
    date_of_the_match = models.DateTimeField()
    main_judge = models.CharField(max_length=50)
    first_assistant_of_sud = models.CharField(max_length=50)
    second_assistant_of_sud = models.CharField(max_length=50)
    delegate_of_the_match = models.CharField(max_length=50)


class Goals(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "goals"
        verbose_name = "Goals"
        verbose_name_plural = "Goals"

    match = models.ForeignKey(Match)
    goal_time = models.IntegerField()
    player = models.ForeignKey(Players)
    own_goal = models.BooleanField()
    penalties = models.BooleanField()


class Cards(models.Model):
    def __unicode__(self):
        return unicode(self.type) or u''

    class Meta:
        db_table = "cards"
        verbose_name = "Card"
        verbose_name_plural = "cards"

    CARD_CHOICES = (
        ('Желтая', 'Желтая'),
        ('Красная', 'Красная'),
    )

    match = models.ForeignKey(Match)
    time = models.TimeField()
    player = models.ForeignKey(ClubPlayers)
    type = models.CharField(max_length=20, choices=CARD_CHOICES)
