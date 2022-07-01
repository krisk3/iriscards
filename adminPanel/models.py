from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=100, unique=True)
    vcffile= models.FileField(upload_to='contact/', null=True, blank=False, verbose_name="Contact File", unique=True)

    def __str__(self):
        return self.name
        
@receiver(pre_delete, sender=Contact)
def Contact_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.vcffile.delete(False)
