from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from .models import Contact

@receiver(post_save, sender=User)
def create_user_contact(sender, instance, created, **kwargs):
    url = f"https://profile.iriscards.com/{instance.email}"
    if created:
        Contact.objects.create(user=instance, email=instance.email, url=url)
