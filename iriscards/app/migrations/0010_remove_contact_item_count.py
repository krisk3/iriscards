# Generated by Django 3.2 on 2023-02-06 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20230206_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='item_count',
        ),
    ]