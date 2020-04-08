from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import TrackRecord, CovidCase, ScreenTime
from ..serializers.beiwe import ScreenTimeSerializer
from ..serializers.info import CovidCaseSerializer
from ..serializers.tracker import TrackerRecordSerializer


class OverviewView(APIView):
    def get(self, request):
        username = request.user
        records = TrackerRecordSerializer(TrackRecord.objects.filter(user__username=username), many=True).data
        covid_cases = CovidCaseSerializer(CovidCase.objects.last()).data
        # TODO: add API to connect patient to user
        bewei = {
            'ScreenTime': ScreenTimeSerializer(ScreenTime.objects.filter(patient__patient_id='12345678'),
                                               many=True).data
        }
        return Response(data={
            'tracker': records,
            'covid_cases': {
                **covid_cases
            },
            'bewei': {
                **bewei
            }
        }, status=status.HTTP_200_OK)
