from crispy_forms.helper import FormHelper
from django import forms
from django.db import models

from blogs.models import Blog, Post
from comments.models import Comment
from crispy_forms.helper import FormHelper
from ckeditor.widgets import CKEditorWidget



class BlogForm(forms.ModelForm):
    helper = FormHelper()
    class Meta:
        model = Blog
        fields = ('title', 'description', 'categories')

class PostForm(forms.ModelForm):
    helper = FormHelper()
    class Meta:
        model = Post
        fields = ('title', 'content', 'blog')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)



class SortForm(forms.Form):
    helper = FormHelper()
    sort = forms.ChoiceField(choices=(('title', u'Title'), ('description', u'Description')))
    search = forms.CharField(required=False)

