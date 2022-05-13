from django.db import models
from .author import Author
from .category import Category
from .tag import Tag

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=50)
#    header_image = models.ImageField(upload_to="postimages")
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories", default=None)
    tag = models.ManyToManyField(Tag, related_name="posttag")
    image_url = models.URLField()
    approved = models.BooleanField(default=False)