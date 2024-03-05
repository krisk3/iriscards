from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
import mimetypes


from app.models import Contact as ContactModel
#from app.utils import Util

#from api.serializers import ContactSerializer, ProfilePicSerializer, BrochureSerializer, ProfileAndBrochureSerializer
from .serializers import LoginSerializer

from rest_framework import permissions, status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes as permclass

import os
from django.conf import settings

# Create your views here.

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        return Response({"email":user.email, "detail": "Login Successful"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permclass([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response('User Logged out successfully')
