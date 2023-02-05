# Generated by Django 3.2 on 2023-02-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('item_count', models.PositiveSmallIntegerField(default=2)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Profile Pic')),
                ('contact_file', models.FileField(blank=True, upload_to='profile/', verbose_name='Contact File')),
                ('email2', models.EmailField(max_length=100)),
                ('phone2', models.CharField(max_length=15)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6)),
                ('location', models.URLField(blank=True, verbose_name='Location')),
                ('linkedinlink', models.URLField(max_length=250, verbose_name='URL')),
                ('twitterlink', models.URLField(max_length=250, verbose_name='URL')),
                ('facebooklink', models.URLField(max_length=250, verbose_name='URL')),
                ('instagramlink', models.URLField(max_length=250, verbose_name='URL')),
                ('skypelink', models.URLField(max_length=250, verbose_name='URL')),
                ('youtubelink', models.URLField(max_length=250, verbose_name='URL')),
                ('brochure_file', models.FileField(blank=True, upload_to='brochure/', verbose_name='Brochure File')),
                ('about', models.TextField()),
            ],
        ),
    ]
