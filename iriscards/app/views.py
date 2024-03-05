from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
import mimetypes


from app.models import Contact as ContactModel
from user.models import User
#from app.utils import Util

from app.serializers import ContactSerializer#, ProfilePicSerializer, BrochureSerializer, ProfileAndBrochureSerializer
# from api.serializers import LoginSerializer as LoginSerial

from rest_framework import permissions, status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes as permclass

import os
from django.conf import settings

# Create your views here.
class ProfileDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer

    def get(self, request, email):
        user = User.objects.get(email=email)
        return self.queryset.get(request, user=user)

class ProfileEditView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    #permission_classes = [IsAuthenticated]
    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)
