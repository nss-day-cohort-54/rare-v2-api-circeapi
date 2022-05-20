from django.db import models
from django.contrib.auth.models import User

# from .photo import Photo
# from rareapi.views.photo import PhotoSerializer

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # @property
    # def profileImageUrl(self):
    #     """profile image for user"""
    #     photo = PhotoSerializer(Photo.objects.filter(author = self).last())
    #     return photo
        
        