import sys

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Survey, Accelerometer, GPS, Identifier, Proximity, Reachability, ScreenTime
from ..serializers.beiwe import BeiweSerializer


# This is for super user to submit Beiwe data
class BeiweDataSubmit(APIView):
    def post(self, request):
        serializer = BeiweSerializer(data=request.data)
        if serializer.is_valid():
            json_data = serializer.validated_data
            patient_id = json_data['patient_id']
            mapping = {
                'survey': Survey,
                'accelerometer': Accelerometer,
                'gps': GPS,
                'identifiers': Identifier,
                'proximity': Proximity,
                'reachability': Reachability,
                'screen_time': ScreenTime
            }
            for key, cls in mapping.items():
                if key in json_data:
                    for item in json_data[key]:
                        obj = cls(patient=patient_id, **item)
                        print(obj, file=sys.stderr)
                        obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
