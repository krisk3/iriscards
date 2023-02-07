from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import logout
from app.models import Contact as ContactModel
from api.serializers import ContactSerializer
from api.serializers import LoginSerializer as LoginSerial
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions, serializers
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes as pclass
# Create your views here.

class ContactCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer

    def post(self, request):
        return self.create(request)


class ProfileDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)


class ProfileEditView(mixins.UpdateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer

    def put(self, request, pk):
        return self.update(request, pk)


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    queryset=ContactModel.objects.all()
    serializer_class=ContactSerializer


    def post(self, request, format=None):
        serializer = LoginSerial(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        con = ContactModel.objects.get(email=user.username)
        print(con.email)
        retval = {"username":user.username,"email":con.email}
        print(retval)
        return Response(retval, status=status.HTTP_202_ACCEPTED)


# def get_username(request):
#         if request.user.is_authenticated():
#             username_email = request.user.username
#             return username_email

# def get_url_email(self, request, *args, **kwargs):
#         url_email = self.kwargs['pk']
#         return url_email


@api_view(["GET"])
@pclass([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response('User Logged out successfully')


#Generate VCF Contact File
@api_view(["GET"])
def create_contact(request, pk):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=contact.vcf'

    line = '''BEGIN:VCARD
VERSION:3.0
FN:*first_name* *last_name*
N:;*first_name*;*last_name*;;
EMAIL;TYPE=INTERNET;TYPE=WORK:*email*
EMAIL;TYPE=INTERNET:
TEL;TYPE=WORK:*phone*
TEL:
item1.ADR:;*address_line2*;*address_line1*;*city*;*state*;*zipcode*;*country*;*address_line1*\n*address_line2*\n*city*\, *state* *zipcode*\n*country*
item1.X-ABLabel:
item2.ORG:*company*
item2.X-ABLabel:
item3.TITLE:*job_title*
item3.X-ABLabel:
item4.URL:
item4.X-ABLabel:Location
item5.URL:
item5.X-ABLabel:Linkedin
item6.URL:
item6.X-ABLabel:Twitter
item7.URL:
item7.X-ABLabel:Facebook
item8.URL:
item8.X-ABLabel:Instagram
item9.URL:
item9.X-ABLabel:Skype
item10.URL:
item10.X-ABLabel:Youtube
item11.URL:
item11.X-ABLabel:Website
NOTE:
CATEGORIES:myContacts
END:VCARD'''

    filename = 'contact.vcf'
    obj = ContactModel.objects.get(email=pk)

    if obj.first_name and obj.last_name:
        search_text = '''FN:*first_name* *last_name*
N:;*first_name*;*last_name*;;'''
        replace_text = f'''FN:{obj.first_name} {obj.last_name}
N:;{obj.first_name};{obj.last_name};;'''
        line = line.replace(search_text,replace_text)

    if obj.email:
        search_text = '''EMAIL;TYPE=INTERNET;TYPE=WORK:*email*'''
        replace_text = f'''EMAIL;TYPE=INTERNET;TYPE=WORK:{obj.email}'''
        line = line.replace(search_text,replace_text)

    if obj.phone:
        search_text = '''TEL;TYPE=WORK:*phone*'''
        replace_text = f'''TEL;TYPE=WORK:{obj.phone}'''
        line = line.replace(search_text,replace_text)

    if obj.company:
        search_text = '''item2.ORG:*company*
    item2.X-ABLabel:'''
        replace_text = f'''item2.ORG:{obj.company}
    item2.X-ABLabel:'''
    line = line.replace(search_text,replace_text)

    if obj.job_title:
        search_text = '''item3.TITLE:*job_title*
    item3.X-ABLabel:'''
        replace_text = f'''item3.TITLE:{obj.job_title}
    item3.X-ABLabel:'''
    line = line.replace(search_text,replace_text)

    if obj.address_line1 and obj.address_line2 and obj.city:
        print("Inside Address")
        search_text = '''item1.ADR:;*address_line2*;*address_line1*;*city*;*state*;*zipcode*;*country*;*address_line1*\n*address_line2*\n*city*\, *state* *zipcode*\n*country*
item1.X-ABLabel:'''
        replace_text = f'''item1.ADR:;{obj.address_line2};{obj.address_line1};{obj.city};{obj.state};{obj.zipcode};{obj.country};{obj.address_line1}\n{obj.address_line2}\n{obj.city}\, {obj.state} {obj.zipcode}\n{obj.country}
    item1.X-ABLabel:'''
    line = line.replace(search_text,replace_text)

    if obj.email2:
        search_text = '''EMAIL;TYPE=INTERNET:'''
        replace_text = f'''EMAIL;TYPE=INTERNET:TYPE=OTHER:{obj.email2}'''
        line = line.replace(search_text,replace_text)

    if obj.phone2:
        search_text = '''TEL:'''
        replace_text = f'''TEL:TYPE=OTHER:{obj.phone2}'''
        line = line.replace(search_text,replace_text)

    if obj.location:
        search_text = '''item4.URL:
    item4.X-ABLabel:Location'''
        replace_text = f'''item4.URL:{obj.location}
    item4.X-ABLabel:Location'''
    line = line.replace(search_text,replace_text)

    if obj.website:
        search_text = '''item11.URL:
    item11.X-ABLabel:Website'''
        replace_text = f'''item11.URL:{obj.website}
    item11.X-ABLabel:Website'''
    line = line.replace(search_text,replace_text)

    if obj.linkedinlink:
        search_text = '''item5.URL:
    item5.X-ABLabel:Linkedin'''
        replace_text = f'''item5.URL:{obj.linkedinlink}
    item5.X-ABLabel:Linkedin'''
    line = line.replace(search_text,replace_text)

    if obj.twitterlink:
        search_text = '''item6.URL:
    item6.X-ABLabel:Twitter'''
        replace_text = f'''item6.URL:{obj.twitterlink}
    item6.X-ABLabel:Twitter'''
    line = line.replace(search_text,replace_text)

    if obj.facebooklink:
        search_text = '''item7.URL:
    item7.X-ABLabel:Facebook'''
        replace_text = f'''item7.URL:{obj.facebooklink}
    item7.X-ABLabel:Facebook'''
    line = line.replace(search_text,replace_text)

    if obj.skypelink:
        search_text = '''item9.URL:
    item9.X-ABLabel:Skype'''
        replace_text = f'''item9.URL:{obj.skypelink}
    item9.X-ABLabel:Skype'''
    line = line.replace(search_text,replace_text)

    if obj.youtubelink:
        search_text = '''item10.URL:
    item10.X-ABLabel:Youtube'''
        replace_text = f'''item10.URL:{obj.youtubelink}
    item10.X-ABLabel:Youtube'''
    line = line.replace(search_text,replace_text)

    response.writelines(line)
    return response




