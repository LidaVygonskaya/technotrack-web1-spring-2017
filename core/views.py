from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

from blogs.models import Blog, Post
from comments.models import Comment


class HomePageView(TemplateView):
    template_name = "core/home.html"

