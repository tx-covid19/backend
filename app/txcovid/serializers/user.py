from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)
    postal_code = serializers.CharField(max_length=5, min_length=5, required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password', 'postal_code')
        extra_kwargs = {'password': {'write_only': True}}
