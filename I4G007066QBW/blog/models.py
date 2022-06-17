from turtle import mode, title
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField('date published')
    published_date = models.DateTimeField('date published')
