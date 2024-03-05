from rest_framework import serializers
from app.models import Contact

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email',]

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['user',
                'first_name',
                'last_name',
                'company',
                'job_title',
                'email',
                'phone',
                'profile_pic',

                'email2',
                'phone2',

                'address_line1',
                'address_line2',
                'city',
                'state',
                'country',
                'zipcode',
                'location',

                'website',
                'linkedinlink',
                'twitterlink',
                'facebooklink',
                'instagramlink',
                'skypelink',
                'youtubelink',

                'brochure_file',
                ]