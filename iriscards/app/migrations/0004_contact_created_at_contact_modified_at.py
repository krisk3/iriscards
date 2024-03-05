# Generated by Django 4.2.8 on 2024-03-04 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_contact_phone_alter_contact_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contact",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
