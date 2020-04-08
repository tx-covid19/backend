from rest_framework import serializers

from ..models import Survey, Accelerometer, GPS, Identifier, Proximity, Reachability, ScreenTime


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class AccelerometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accelerometer
        fields = '__all__'


class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPS
        fields = '__all__'


class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = '__all__'


class ProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proximity
        fields = '__all__'


class ReachabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reachability
        fields = '__all__'


class ScreenTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenTime
        fields = '__all__'
