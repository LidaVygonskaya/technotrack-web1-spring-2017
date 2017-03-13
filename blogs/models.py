from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Blog(models.Model):

    owner = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Post(models.Model):
    blog = models.ForeignKey('blogs.Blog')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)