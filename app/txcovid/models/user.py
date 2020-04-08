from django.db import models
from django.contrib.auth.models import AbstractUser


class Participant(AbstractUser):
    # TODO add more detailed address
    address = models.TextField(blank=True)
