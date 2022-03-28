from django.conf import settings
from django.db import models
from django.utils import timezone


class WritingInfo(models.Model):
    writing_id = models.IntegerField(blank=True)
    word_count = models.IntegerField(blank=True)
    time_spent = models.IntegerField(blank=True) #Time spent on writing in seconds
    created_at = models.DateTimeField(default=timezone.now)

    #set method to get all time for writing id and subtract from params value. Remainder is persisted to DB

    #set method to get all words for writing id and subtract from prams value. Remainder is persisted to DB

class WritingTotals(models.Model):
    writing_id = models.IntegerField(blank=True)
    total_words = models.IntegerField(blank=True)
    total_time_in_seconds = models.IntegerField(blank=True) #Time spent on writing in seconds
