from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from ..models import Event, User
from ..serializers.event import EventSerializer


class EventView(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username__exact=request.user)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            record = Event(user=user, **request.data)
            record.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
