from rest_framework import serializers
from ..models import CovidCase


class CovidCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCase
        exclude = ['counties_json']
