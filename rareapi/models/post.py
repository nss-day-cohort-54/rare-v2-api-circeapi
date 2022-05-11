from django.db import models
from .author import Author

class Post(models.Model):
    title = models.CharField(max_length=50)
#    header_image = models.ImageField(upload_to="postimages")
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
#    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
