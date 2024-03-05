"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from . import models
from .models import FirstPassword, User
from .forms import UserAdminForm

from import_export.admin import ImportExportModelAdmin

import random
import string

def generate_password(length=3):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    """
    Custom UserAdmin class to define the admin pages for managing user models.

    This class extends the Django BaseUserAdmin class to customize the admin interface
    for the User model.
    """
    add_form = UserAdminForm
    ordering = ["-modified_at"]
    list_display = ["email",]
    fieldsets = (
        (None, {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "modified_at",
                )
            },
        ),
    )
    readonly_fields = [
        "last_login",
        "created_at",
        "modified_at",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            print("User already created")
        except:
            if not password:
                password = f"Pass#{random.randint(0, 9)}{generate_password(3)}"
                obj.set_password(password)
            else:
                obj.set_password(password)
            super().save_model(request, obj, form, change)

            user = User.objects.get(email=email)
            first_password = FirstPassword.objects.create(user=user, password=password)
            first_password.save()

            message = f"""Dear User,

Welcome to IrisCards! We are delighted to welcome you to our community of futuristic users who use next-generation NFC-based cards to seamlessly exchange information.

Your account has been successfully created, and below are your login details:

Username: {email}
Password: {password}

To get started, please click the link below and enter your card information.
https://profile.iriscards.com/

You can effortlessly update the information stored on your NFC business card at any time in the future simply by using your unique username and password.
If you have any questions or need assistance, don't hesitate to reach out to us at manager@iriscards.com . We're here to help you every step of the way.

Thank you for choosing Iris Cards. We are excited to simplify your business networking experience.

Best regards,
Marketing Coordinator
Iris Cards"""
            send_mail("Welcome to Iris Cards", message, "IRIS CARDS <manager@iriscards.com>", [email])
            print("Email sent")


class FirstPasswordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = [
        "user",
        "password",
    ]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.FirstPassword, FirstPasswordAdmin)
admin.site.unregister(Group)
