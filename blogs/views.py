from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Blog, Post


# Create your views here.

class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    queryset = Blog.objects.all()
    count = Blog.objects.all().count()
class BlogDetail(DetailView):
    template_name = "blogs/blog.html"
    queryset = Blog.objects.all()
    pk_url_kwarg = "blog_id"

class PostDetail(DetailView):
    template_name = "blogs/post.html"
    queryset = Post.objects.all()
    pk_url_kwarg = "post_id"
