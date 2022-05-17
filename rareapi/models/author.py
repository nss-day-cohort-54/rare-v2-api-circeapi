from django.db import models
from django.contrib.auth.models import User

from rareapi.models.post import Post


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatarimages")
    
    @property
    def user_posts(self):
        """All posts by user"""
        posts = Post.objects.filter(post=self)