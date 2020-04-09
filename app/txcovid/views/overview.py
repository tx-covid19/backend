import zipcodes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import TrackRecord, CovidCase, ScreenTime, UserPatientRelation, Survey, Accelerometer, GPS, Identifier, \
    Proximity, Reachability, User
from ..serializers.beiwe import SurveySerializer, AccelerometerSerializer, GPSSerializer, \
    IdentifierSerializer, ProximitySerializer, ReachabilitySerializer, ScreenTimeSerializer
from ..serializers.info import CovidCaseSerializer
from ..serializers.tracker import TrackerRecordSerializer


class OverviewView(APIView):
    def _get_beiwe(self, user):
        if not UserPatientRelation.objects.filter(user__username=user).exists():
            return {}
        patient_id = UserPatientRelation.objects.get(user__username=user).patient_id
        data = {
            'patient_id': patient_id,
            'survey': SurveySerializer(Survey.objects.filter(patient=patient_id), many=True).data,
            'accelerometer': AccelerometerSerializer(Accelerometer.objects.filter(patient=patient_id), many=True).data,
            'gps': GPSSerializer(GPS.objects.filter(patient=patient_id), many=True).data,
            'identifiers': IdentifierSerializer(Identifier.objects.filter(patient=patient_id), many=True).data,
            'proximity': ProximitySerializer(Proximity.objects.filter(patient=patient_id), many=True).data,
            'reachability': ReachabilitySerializer(Reachability.objects.filter(patient=patient_id), many=True).data,
            'screen_time': ScreenTimeSerializer(ScreenTime.objects.filter(patient=patient_id), many=True).data
        }
        return data

    def get(self, request):
        username = request.user

        records = TrackerRecordSerializer(TrackRecord.objects.filter(user__username=username), many=True).data

        covid_cases = CovidCase.objects.latest('timestamp')
        postal = User.objects.get(username=username).postal_code
        local_info = {}
        if zipcodes.matching(postal):
            county = zipcodes.matching(postal)[0]['county']
            county_name = county.split(' ')[0]
            if county_name in covid_cases.counties_json:
                local_info['local_cases'] = covid_cases.counties_json[county_name]['total']
                local_info['local_deaths'] = covid_cases.counties_json[county_name]['deaths']

        return Response(data={
            'tracker': records,
            'covid_cases': {
                **CovidCaseSerializer(covid_cases).data,
                **local_info
            },
            'bewei': {
                **self._get_beiwe(username)
            }
        }, status=status.HTTP_200_OK)
