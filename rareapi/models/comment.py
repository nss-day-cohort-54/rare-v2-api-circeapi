from django.db import models


class Comment(models.Model):
    post = models.ForeignKey("post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("author", on_delete=models.CASCADE, related_name="comments")
    subject = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)