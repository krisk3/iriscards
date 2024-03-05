from django.contrib import admin
from .models import Contact
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    exclude = ('user',)
    ordering = ["-modified_at"]
    readonly_fields = [
        "email",
        "url",
    ]

admin.site.register(Contact, ContactAdmin)
