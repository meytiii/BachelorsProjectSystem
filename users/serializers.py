from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import karbar
import logging

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    sid = serializers.IntegerField(read_only=True)
    is_professor = serializers.BooleanField(read_only=True)
    logger = logging.getLogger(__name__)
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if user and user.is_active and isinstance(user, karbar):
                data['sid'] = user.sid
                data['first_name'] = user.first_name
                data['last_name'] = user.last_name
                data['is_professor'] = user.is_professor

                return data
            else:
                raise serializers.ValidationError('Invalid username or password')
        else:
            raise serializers.ValidationError('Username and password are required')