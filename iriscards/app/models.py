from django.db import models
from user.models import User
# # Create your models here.

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True, verbose_name="Profile Pic")

    url = models.URLField(max_length=255, blank=True, verbose_name="URL")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    email2 = models.EmailField(max_length=100, verbose_name="Secondary Email", blank=True)
    phone2 = models.CharField(max_length=15, verbose_name="Secondary Phone", blank=True)

    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=6, blank=True)
    location = models.URLField(max_length=250, blank=True, verbose_name="Location")

    website = models.URLField(max_length=250, verbose_name="Website", blank=True )
    linkedinlink = models.URLField(max_length=250, verbose_name="Linkedin", blank=True)
    twitterlink = models.URLField(max_length=250, verbose_name="Twitter", blank=True)
    facebooklink = models.URLField(max_length=250, verbose_name="Facebook", blank=True)
    instagramlink = models.URLField(max_length=250, verbose_name="Instagram", blank=True)
    skypelink = models.URLField(max_length=250, verbose_name="Skype", blank=True)
    youtubelink = models.URLField(max_length=250, verbose_name="Youtube", blank=True)

    brochure_file = models.FileField(upload_to='brochure/', blank=True, null=True, verbose_name="Brochure File")


    def __str__(self):
        if not (self.first_name or self.last_name or self.company):
            retval = f"{self.email}"
        elif not (self.company):
            retval = f"{self.email} - {self.first_name} {self.last_name}"
        else:
            retval = f"{self.email} - {self.first_name} {self.last_name} - {self.company}"
        return retval
