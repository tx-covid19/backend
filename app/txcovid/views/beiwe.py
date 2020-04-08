from cerberus import Validator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Survey, Accelerometer, GPS, Identifier, Proximity, Reachability, ScreenTime, UserPatientRelation
from ..serializers.beiwe import ScreenTimeSerializer

req_schema = {
    'patient_id': {
        'type': 'string',
        'required': True
    },
    'survey': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'survey_id': {'type': 'string', 'required': True, 'maxlength': 8},
                'begin_timestamp': {'type': 'integer', 'required': True},
                'end_timestamp': {'type': 'integer', 'required': True},
                'answers': {'type': 'string', 'required': True},
                'num_scheduled': {'type': 'integer', 'required': True, 'min': 0},
                'num_completed': {'type': 'integer', 'required': True, 'min': 0}
            }
        }
    },
    'accelerometer': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'begin_timestamp': {'type': 'integer', 'required': True},
                'end_timestamp': {'type': 'integer', 'required': True},
                'duration_phone_on_person': {'type': 'integer', 'required': True, 'min': 0},
                'duration_sedentary': {'type': 'integer', 'required': True, 'min': 0}
            }
        }
    },
    'gps': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'type': 'dict',
                'schema': {
                    'begin_timestamp': {'type': 'integer', 'required': True},
                    'end_timestamp': {'type': 'integer', 'required': True},
                    'number_locations_visited': {'type': 'integer', 'required': True, 'min': 0},
                    'travel_radius_miles_mean': {'type': 'number', 'required': True},
                    'travel_radius_miles_sum_product': {'type': 'number', 'required': True},
                    'travel_radius_miles_sum_squares': {'type': 'number', 'required': True},
                    'path_length_miles': {'type': 'integer', 'required': True, 'min': 0},
                    'num_data_points': {'type': 'integer', 'required': True, 'min': 0}
                }
            }
        }
    },
    'identifiers': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'begin_timestamp': {'type': 'integer', 'required': True},
                'end_timestamp': {'type': 'integer', 'required': True},
                'phone_version': {'type': 'string', 'required': True},
                'phone_model': {'type': 'string', 'required': True},
                'phone_manufacturer': {'type': 'string', 'required': True},
                'operating_system': {'type': 'string', 'required': True},
                'operating_system_version': {'type': 'string', 'required': True}
            }
        }
    },
    'proximity': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'begin_timestamp': {'type': 'integer', 'required': True},
                'end_timestamp': {'type': 'integer', 'required': True},
                'duration_on_phone': {'type': 'integer', 'required': True, 'min': 0}
            }
        }
    },
    'reachability': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'begin_timestamp': {'type': 'integer', 'required': True},
                'end_timestamp': {'type': 'integer', 'required': True},
                'duration_wifi': {'type': 'integer', 'required': True, 'min': 0}
            }
        }
    },
    'screen_time': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'begin_timestamp': {'type': 'integer', 'required': True},
                'end_timestamp': {'type': 'integer', 'required': True},
                'duration_screen_unlocked': {'type': 'integer', 'required': True, 'min': 0}
            }
        }
    }
}


class BeiweDataView(APIView):
    def get(self, request):
        # TODO: put into serializer
        res = {
            'ScreenTime': ScreenTimeSerializer(ScreenTime.objects.filter(patient__patient_id='12345678'),
                                               many=True).data
        }
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        json_data = request.data
        validator = Validator()
        if not validator.validate(json_data, req_schema):
            return Response('. '.join([f'{k}: {",".join(errs)}' for k, errs in validator.errors.items()]),
                            status=status.HTTP_400_BAD_REQUEST)

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
                    obj = cls(patient=UserPatientRelation.objects.get(user__username=request.user), **item)
                    obj.save()

        return Response({'status': True}, status=status.HTTP_201_CREATED)
