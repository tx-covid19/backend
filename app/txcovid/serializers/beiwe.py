from rest_framework import serializers

from ..models import Survey, Accelerometer, GPS, Identifier, Proximity, Reachability, ScreenTime


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        exclude = ['id', 'patient']


class AccelerometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accelerometer
        exclude = ['id', 'patient']


class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPS
        exclude = ['id', 'patient']


class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        exclude = ['id', 'patient']


class ProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proximity
        exclude = ['id', 'patient']


class ReachabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reachability
        exclude = ['id', 'patient']


class ScreenTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenTime
        exclude = ['id', 'patient']


class BeiweSerializer(serializers.Serializer):
    patient_id = serializers.CharField(max_length=8)
    survey = SurveySerializer(many=True, required=False)
    accelerometer = AccelerometerSerializer(many=True, required=False)
    gps = AccelerometerSerializer(many=True, required=False)
    identifiers = IdentifierSerializer(many=True, required=False)
    proximity = ProximitySerializer(many=True, required=False)
    reachability = ProximitySerializer(many=True, required=False)
    screen_time = ScreenTimeSerializer(many=True, required=False)
