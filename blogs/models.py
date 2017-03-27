from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Blog(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Categories)



class Post(models.Model):
    blog = models.ForeignKey('blogs.Blog')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blogs.Post')

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __unicode__(self):
        return self.category
