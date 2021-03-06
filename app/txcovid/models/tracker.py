from django.db import models

from .user import User


class TrackRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    track_date = models.DateField(unique=True)
    cost_category = models.CharField(max_length=100)
    cost = models.FloatField()

    people_interacted = models.PositiveIntegerField()
    screen_time = models.PositiveIntegerField()
    mood = models.CharField(max_length=20)

    weight = models.FloatField()
    temperature = models.FloatField()
