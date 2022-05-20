from django.db import models
from django.contrib.auth.models import User

# from rareapi.models.post import Post


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
# @property
# def post_count(self):
#     """post count for users view"""
#     postCount = Post.objects.filter(author=self)
    
#     if len(postCount) > 0:
#         post_count = len(postCount)  
#         return post_count
# from .photo import Photo
# from rareapi.views.photo import PhotoSerializer


    
    # @property
    # def profileImageUrl(self):
    #     """profile image for user"""
    #     photo = PhotoSerializer(Photo.objects.filter(author = self).last())
    #     return photo
        
        
