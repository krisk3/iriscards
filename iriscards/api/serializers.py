from rest_framework import serializers
from app.models import Contact

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name',
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

                'about'
                ]
        

class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['profile_pic']


class BrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['brochure_file']

class ProfileAndBrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['profile_pic', 'brochure_file']

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


