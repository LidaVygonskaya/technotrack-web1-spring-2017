from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from comments.models import Comment



class CommentDetail(DetailView):
    template_name = "comments/comment.html"
    queryset = Comment.objects.all()
    pk_url_kwarg = "comment_id"