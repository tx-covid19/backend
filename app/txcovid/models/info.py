# from django.contrib.postgres.fields import JSONField
from django.db import models


# TODO add json field back
class CovidCase(models.Model):
    nation_total = models.PositiveIntegerField()
    nation_deaths = models.PositiveIntegerField()
    tx_total = models.PositiveIntegerField()
    tx_deaths = models.PositiveIntegerField()
    # counties_json = JSONField()
