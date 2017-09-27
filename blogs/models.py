from __future__ import unicode_literals
import json
from django.core.serializers import json
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __unicode__(self):
        return self.category


class Blog(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title




class Post(models.Model):

    blog = models.ForeignKey('blogs.Blog')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    content = RichTextField()
    date_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blogs.Post')

