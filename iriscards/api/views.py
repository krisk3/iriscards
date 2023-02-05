from django.shortcuts import render
from app.models import Contact as ContactModel
from api.serializers import ContactSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class ProfileDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer

    # def get_object(self, email):
    #     try:
    #         return ContactModel.object.get(email=email)
    #     except ContactModel.DoesNotExist:
    #         raise Http404

    def get(self, request, pk):
        # contact = self.get_object(email)
        # serializer = ContactSerializer(contact)
        return self.retrieve(request, pk)


