from datetime import date

from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers, status
from rest_framework.response import Response
# from rest_framework.utils import json
import json
from rest_framework.views import APIView
from django.contrib.auth.models import update_last_login
from .serializers import Users_serializers, Register_User_serializera

from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication, JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from .models import CustomUser


# Create your views here.
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLogin(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)
        if user is None:
            queryset = CustomUser.objects.filter(email = email)
            data = Register_User_serializera(queryset, many= True)
            if password == data.data[0]['password']:
                jwt_token = JWT_ENCODE_HANDLER(email)
                return Response({'email': email, "token":jwt_token})
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return Response({
            'email': user.email,
            'token': jwt_token
        })


class get_users(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        user_data = CustomUser.objects.all()
        serializer = Users_serializers(user_data, many = True)
        return Response({"user_details":serializer.data})


class Register_User(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        serializer = Register_User_serializera(data =data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)