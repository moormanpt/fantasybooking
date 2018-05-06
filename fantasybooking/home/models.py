from django.db import models  # NOQA

from django_extensions.db.models import AutoSlugField  # NOQA
from model_utils.models import TimeStampedModel  # NOQA
from fantasybooking.account.models import User

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
