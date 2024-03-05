from django import forms
from django.contrib.auth.models import User
from user import models

class UserAdminForm(forms.ModelForm):
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)

    class Meta:
        model = models.User
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            if not password1:
                raise forms.ValidationError("Password1 is required if password2 is provided")
            if not password2:
                raise forms.ValidationError("Password2 is required if password1 is provided")
