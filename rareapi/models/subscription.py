from django.db import models


class Subscription(models.Model):
    author = models.ForeignKey("author", on_delete=models.CASCADE, related_name="authors")
    follower = models.ForeignKey("author", on_delete=models.CASCADE, related_name="subscriber")
    created_on = models.DateTimeField(auto_now=True)