from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # TODO add more detailed address
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    postal_code = models.CharField(max_length=5)
