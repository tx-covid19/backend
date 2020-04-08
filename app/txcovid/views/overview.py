from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import sys
from ..models import TrackRecord, CovidCase, ScreenTime, UserPatientRelation, Survey, Accelerometer, GPS, Identifier, \
    Proximity, Reachability
from ..serializers.beiwe import BeiweSerializer
from ..serializers.info import CovidCaseSerializer
from ..serializers.tracker import TrackerRecordSerializer


class OverviewView(APIView):
    def _get_beiwe(self, user):
        if not UserPatientRelation.objects.filter(user__username=user).exists():
            return {}
        patient_id = UserPatientRelation.objects.get(user__username=user).patient_id
        serializers = BeiweSerializer(data={
            'patient_id': patient_id,
            'survey': list(Survey.objects.filter(patient=patient_id)),
            'accelerometer': list(Accelerometer.objects.filter(patient=patient_id)),
            'gps': list(GPS.objects.filter(patient=patient_id)),
            'identifiers': list(Identifier.objects.filter(patient=patient_id)),
            'proximity': list(Proximity.objects.filter(patient=patient_id)),
            'reachability': list(Reachability.objects.filter(patient=patient_id)),
            'screen_time': list(ScreenTime.objects.filter(patient=patient_id))
        })
        if serializers.is_valid():
            return serializers.data
        else:
            return {}

    def get(self, request):
        username = request.user

        records = TrackerRecordSerializer(TrackRecord.objects.filter(user__username=username), many=True).data
        covid_cases = CovidCaseSerializer(CovidCase.objects.latest('timestamp')).data
        return Response(data={
            'tracker': records,
            'covid_cases': {
                **covid_cases
            },
            'bewei': {
                **self._get_beiwe(username)
            }
        }, status=status.HTTP_200_OK)
