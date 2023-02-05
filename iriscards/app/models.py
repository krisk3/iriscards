from django.db import models
# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    item_count = models.PositiveSmallIntegerField(default=2)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name="Profile Pic") #Add default value
    contact_file = models.FileField(upload_to='profile/', blank=True, verbose_name="Contact File") #Add default value - Also check one-one field for Contact file

    email2 = models.EmailField(max_length=100, verbose_name="Secondary Email", blank=True)
    phone2 = models.CharField(max_length=15, verbose_name="Secondary Phone", blank=True)

    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=6, blank=True)
    location = models.URLField(max_length=200, blank=True, verbose_name="Location")

    linkedinlink = models.URLField(max_length=250, verbose_name="Linkedin", blank=True)
    twitterlink = models.URLField(max_length=250, verbose_name="Twitter", blank=True)
    facebooklink = models.URLField(max_length=250, verbose_name="Facebook", blank=True)
    instagramlink = models.URLField(max_length=250, verbose_name="Instagram", blank=True)
    skypelink = models.URLField(max_length=250, verbose_name="Skype", blank=True)
    youtubelink = models.URLField(max_length=250, verbose_name="Youtube", blank=True)

    brochure_file = models.FileField(upload_to='brochure/', blank=True, verbose_name="Brochure File")

    about = models.TextField(blank=True)

    def __str__(self):
        retval = f"{self.first_name} {self.last_name} - {self.company}"
        return retval




