from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField()
    state = serializers.CharField()
    postal_code = serializers.CharField(max_length=5, min_length=5)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'address', 'city', 'state', 'postal_code')
        extra_kwargs = {'password': {'write_only': True}}
