from rest_framework import serializers

from ..models import TrackRecord


class TrackerRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackRecord
        exclude = ['user', 'last_update']
