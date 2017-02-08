# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __builtin__ import unicode
from django.utils import timezone
from .staff import Staff
from .team import Teams
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
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
    season = ChainedForeignKey(Season,
                               chained_field="championship",
                               chained_model_field="championships",
                               show_all=False,
                               auto_choose=True,
                               sort=True)
    tour = models.IntegerField()
    members = models.ManyToManyField(Season,
                                     chained_field="season",
                                     chained_model_field="members")
    host = ChainedForeignKey(Teams,
                             chained_field="season",
                             chained_model_field="members",
                             related_name="host",
                             show_all=False,
                             auto_choose=True,
                             sort=True)
    guests = ChainedForeignKey(Teams,
                               chained_field="season",
                               chained_model_field="members",
                               related_name="guests")
    date_of_the_match = models.DateTimeField()
    main_judge = models.ForeignKey(Staff, related_name="main_judge")
    first_assistant_of_sud = models.ForeignKey(Staff, related_name="first_assistant_of_sud")
    second_assistant_of_sud = models.ForeignKey(Staff, related_name="second_assistant_of_sud")
    delegate_of_the_match = models.ForeignKey(Staff, related_name="delegate_of_the_match")


class Goals(models.Model):
    class Meta:
        db_table = "goals"
        verbose_name = "Goals"
        verbose_name_plural = "Goals"

    match = models.ForeignKey(Match)
    goal_time = models.IntegerField()
    player = models.ForeignKey(Players)
    own_goal = models.BooleanField()
    penalties = models.BooleanField()

    def __unicode__(self):
        return unicode(self.goal_time) or u''


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
