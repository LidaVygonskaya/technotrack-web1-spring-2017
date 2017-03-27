from django import forms
from django.db import models

from blogs.models import Blog, Post
from comments.models import Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'blog')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class SortForm(forms.Form):
    sort = forms.ChoiceField(choices=(('title', u'Title'), ('description', u'Desription')))
    search = forms.CharField(required=False)