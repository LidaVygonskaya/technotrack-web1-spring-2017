from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('blogs.Post')
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)