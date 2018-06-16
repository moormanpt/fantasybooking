from django.db import models  # NOQA

from django_extensions.db.models import AutoSlugField  # NOQA
from model_utils.models import TimeStampedModel  # NOQA
from fantasybooking.account.models import User
from django.contrib import admin

import pdb

# Create your models here.
# Manager, Stable, Wrestler, WeeklyStat

class Stable(models.Model):
    name = models.CharField(max_length=128)
    manager = models.ForeignKey(User)

    def __str__(self):
        return self.name  

class Wrestler(models.Model):
    name = models.CharField(max_length=128)
    stable = models.ForeignKey(Stable)

    def __str__(self):
        return self.name

class WeeklyStat(models.Model):
    card = models.CharField(max_length=128)
    finish = models.IntegerField()
    matchlength = models.DurationField()
    matchdate = models.DateField(auto_now=False, auto_now_add=False)
    wrestler = models.ForeignKey(Wrestler)

    def __str__(self):
        return self.card

class Match(models.Model):
    name = models.CharField(max_length=128)
    champion = models.ForeignKey(Wrestler, related_name='champion', blank=True, null=True)
    challenger = models.ForeignKey(Wrestler, related_name='challenger', blank=True, null=True)
    winner = models.ForeignKey(Wrestler, related_name='winner', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'matches'

    def __str__(self):
        return self.name

    def resolve(self):
        "Provides Finish for a match"
        champion_weekly_stat = WeeklyStat.objects.filter(wrestler=champion).latest()

        challenger_weekly_stat = WeeklyStat.objects.filter(wrestler=challenger).latest()
        
        if champion_weekly_stat.finish >= challenger_weekly_stat.finish:
            return champion
        else:
            return challenger
