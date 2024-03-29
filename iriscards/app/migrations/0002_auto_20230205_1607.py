# Generated by Django 3.2 on 2023-02-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email2',
            field=models.EmailField(max_length=100, verbose_name='Secondary Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='facebooklink',
            field=models.URLField(max_length=250, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='instagramlink',
            field=models.URLField(max_length=250, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='linkedinlink',
            field=models.URLField(max_length=250, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone2',
            field=models.CharField(max_length=15, verbose_name='Secondary Phone'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='skypelink',
            field=models.URLField(max_length=250, verbose_name='Skype'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitterlink',
            field=models.URLField(max_length=250, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='youtubelink',
            field=models.URLField(max_length=250, verbose_name='Youtube'),
        ),
    ]
