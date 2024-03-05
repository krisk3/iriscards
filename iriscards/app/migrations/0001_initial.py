# Generated by Django 4.2.8 on 2024-03-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "email",
                    models.EmailField(
                        max_length=100, primary_key=True, serialize=False
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=100)),
                ("last_name", models.CharField(blank=True, max_length=100)),
                ("company", models.CharField(blank=True, max_length=100)),
                ("job_title", models.CharField(blank=True, max_length=50)),
                ("phone", models.CharField(max_length=15)),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pic/",
                        verbose_name="Profile Pic",
                    ),
                ),
                ("url", models.URLField(max_length=255)),
                (
                    "email2",
                    models.EmailField(
                        blank=True, max_length=100, verbose_name="Secondary Email"
                    ),
                ),
                (
                    "phone2",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="Secondary Phone"
                    ),
                ),
                ("address_line1", models.CharField(blank=True, max_length=100)),
                ("address_line2", models.CharField(blank=True, max_length=100)),
                ("city", models.CharField(blank=True, max_length=100)),
                ("state", models.CharField(blank=True, max_length=50)),
                ("country", models.CharField(blank=True, max_length=50)),
                ("zipcode", models.CharField(blank=True, max_length=6)),
                (
                    "location",
                    models.URLField(
                        blank=True, max_length=250, verbose_name="Location"
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, max_length=250, verbose_name="Website"),
                ),
                (
                    "linkedinlink",
                    models.URLField(
                        blank=True, max_length=250, verbose_name="Linkedin"
                    ),
                ),
                (
                    "twitterlink",
                    models.URLField(blank=True, max_length=250, verbose_name="Twitter"),
                ),
                (
                    "facebooklink",
                    models.URLField(
                        blank=True, max_length=250, verbose_name="Facebook"
                    ),
                ),
                (
                    "instagramlink",
                    models.URLField(
                        blank=True, max_length=250, verbose_name="Instagram"
                    ),
                ),
                (
                    "skypelink",
                    models.URLField(blank=True, max_length=250, verbose_name="Skype"),
                ),
                (
                    "youtubelink",
                    models.URLField(blank=True, max_length=250, verbose_name="Youtube"),
                ),
                (
                    "brochure_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="brochure/",
                        verbose_name="Brochure File",
                    ),
                ),
            ],
        ),
    ]
