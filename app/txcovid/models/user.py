from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    postal_code = models.CharField(max_length=5, null=True)
