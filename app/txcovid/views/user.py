from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import UserPatientRelation, User
from ..serializers.user import UserSerializer


# TODO: view/edit user profile


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            password = validated_data.pop('password', None)

            if User.objects.filter(email=validated_data['email']).exists():
                return Response({'email': 'E-mail exists.'}, status=status.HTTP_303_SEE_OTHER)

            user = User(**validated_data, is_active=False)
            if password is not None:
                user.set_password(password)

            user.save()
            if 'patient_id' in request.data:
                patient_id = request.data['patient_id']
                if len(patient_id) > 8:
                    return Response({"patient": "Bad Id."}, status=status.HTTP_400_BAD_REQUEST)
                if UserPatientRelation.objects.filter(patient_id=patient_id).exists():
                    return Response({'patient': 'Patient ID exists.'}, status=status.HTTP_303_SEE_OTHER)
                UserPatientRelation(user=user, patient_id=patient_id).save()

            return Response(validated_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):
    def get(self, request):
        username = request.user
        return Response(UserSerializer(User.objects.get(username=username)).data)
