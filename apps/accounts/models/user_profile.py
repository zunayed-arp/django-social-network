
import datetime
import os
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from ...accounts.models import User
from ...utils import path_and_rename
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(
        "User", on_delete=models.DO_NOTHING, related_name="profile"
    )
    profile_image = models.ImageField(upload_to="profiles",default="avatars/guest.png")
    cover_image = models.ImageField(upload_to="profiles",default="avatars/cover.png")
    phone = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=20,blank=True)
    country = models.CharField(max_length=20,blank=True)
    
    def __str__(self):
        return self.user.username
        
    
    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url
        return settings.MEDIA_URL + self._meta.get_field('profile_image').get_default()
    
    def get_cover_image(self):
        if self.cover_image:
            return self.cover_image.url
        return settings.MEDIA_URL + self._meta.get_field('cover_image').get_default()    
    
    @receiver(post_save,sender=User)
    def create_profile(sender,**kwargs):
        if kwargs.get('created',False):
            Profile.objects.create(user=kwargs['instance'])
   

    
