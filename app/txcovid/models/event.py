from django.db import models
# from django.contrib.postgres.fields import JSONField

from .user import User


class EventRecord(models.Model):
    """
    Model to track user interaction with the frontend.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    event = models.CharField(max_length=50)
    # metadata = JSONField()
