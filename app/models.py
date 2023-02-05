from datetime import datetime
import random

from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Counter(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def days_since(self):
        return (datetime.now().date() - self.date).days

    def color(self):
        r = lambda: random.randint(0, 140)
        return '#%02X%02X%02X' % (r(), r(), r())

    def __str__(self):
        return self.name
