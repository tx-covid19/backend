# from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator
from django.db import models
from .user import User

id_validator = RegexValidator('^[1-9a-z]+$', message='This field can only contain characters 1-9 and a-z.')


class UserPatientRelation(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    patient_id = models.CharField(max_length=8, validators=[id_validator], unique=True)


class AbstractAggregationModel(models.Model):
    patient = models.ForeignKey(UserPatientRelation, on_delete=models.PROTECT)
    begin_timestamp = models.BigIntegerField()
    end_timestamp = models.BigIntegerField()

    class Meta:
        abstract = True


class Survey(AbstractAggregationModel):
    survey_id = models.CharField(max_length=8)
    # answers = JSONField()
    num_scheduled = models.PositiveIntegerField()
    num_completed = models.PositiveIntegerField()


class Accelerometer(AbstractAggregationModel):
    duration_phone_on_person = models.PositiveIntegerField()
    duration_sedentary = models.PositiveIntegerField()


class GPS(AbstractAggregationModel):
    number_locations_visited = models.PositiveIntegerField()
    travel_radius_miles_mean = models.FloatField()
    travel_radius_miles_sum_product = models.FloatField()
    travel_radius_miles_sum_squares = models.FloatField()
    path_length_miles = models.PositiveIntegerField()
    num_data_points = models.PositiveIntegerField()


class Identifier(AbstractAggregationModel):
    phone_version = models.TextField()
    phone_model = models.TextField()
    phone_manufacturer = models.TextField()
    operating_system = models.TextField()
    operating_system_version = models.TextField()


class Proximity(AbstractAggregationModel):
    duration_on_phone = models.PositiveIntegerField()


class Reachability(AbstractAggregationModel):
    duration_wifi = models.PositiveIntegerField()


class ScreenTime(AbstractAggregationModel):
    duration_screen_unlocked = models.PositiveIntegerField()
