
from .models import Blog, Category, Like
from .models import Post
from django.contrib import admin
from comments.models import Comment
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Like)
#
class CommentForm(forms.ModelForm):
     content3 = forms.CharField(widget=CKEditorWidget(config_name='default'))
     meow = forms.CharField()
     class Meta:
         model = Comment
         fields = ('content',)
         widgets = {
             'content': CKEditorWidget(config_name='default'),
         }
