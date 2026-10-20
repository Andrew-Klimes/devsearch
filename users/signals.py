from django.contrib.auth.models import User
from .models import Profile

from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

def createProfile(sender, instance, created, **kwargs):
    print('Profile signall triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
        
def deleteProfile(sender, instance, **kwargs):
    print('Profile was deleted!')
    user = instance.user
    user.delete()
    
post_save.connect(createProfile, sender=User)
post_delete.connect(deleteProfile, sender=Profile)
            
       