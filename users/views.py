from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import UserLoginSerializer
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .serializers import UserLoginSerializer 
from .models import karbar
import logging
from datetime import datetime, timedelta

def home(request):
    return HttpResponse("Welcome to the home page!")

logger = logging.getLogger(__name__)

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = authenticate(
                request=self.request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )

            if user and isinstance(user, karbar):
                login(request, user)

                token, created = Token.objects.get_or_create(user=user)

                expiration_date = datetime.now() + timedelta(days=3)

                return Response({
                    'token': token.key,
                    'user_sid': user.sid,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_professor': user.is_professor,
                    'token_expiration': expiration_date.isoformat(),
                }, status=status.HTTP_200_OK)
            else:
                print(f"Failed login attempt with username: {serializer.validated_data['username']}")
                print(serializer.errors)
                return Response({'non_field_errors': ['Invalid username or password :D']}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)