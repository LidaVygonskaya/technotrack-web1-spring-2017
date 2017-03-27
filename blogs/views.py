from django import forms
from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView

from blogs.forms import SortForm
from comments.models import Comment
from .models import Blog, Post


# Create your views here.

class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    queryset = Blog.objects.all()
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        queryset = Blog.objects.all()
        if self.sortform.is_valid():
            queryset = queryset.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                queryset = queryset.filter(title__icontains=self.sortform.cleaned_data['search'])

        return queryset

class BlogDetail(DetailView):
    template_name = "blogs/blog.html"
    queryset = Blog.objects.all()

class PostDetail(CreateView):
    template_name = "blogs/post.html"
    model = Comment
    fields = ('content',)
    postobject = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postobject
        return super(PostDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('blogs:postDetail', pk = self.postobject.pk)


class UpdateBlog(UpdateView):
    template_name = 'blogs/editblog.html'
    model = Blog
    fields = ('title', 'description')
    def get_success_url(self):
        return reverse('blogs:blog_list')


    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)

class CreateBlog(CreateView):
    template_name = 'blogs/addblog.html'
    model = Blog
    fields = ('title', 'description')

    def get_success_url(self):
        return reverse('blogs:blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlog, self).form_valid(form)

class UpdatePost(UpdateView):
    template_name = 'blogs/editpost.html'
    model = Post
    fields = ('title', 'content')

    def get_success_url(self):
        return reverse('blogs:blog_list')


    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class CreatePost(CreateView):
    template_name = 'blogs/addpost.html'
    model = Post
    fields = ('title', 'content','blog')

    def get_success_url(self):
        return reverse('blogs:blog_list')

    def get_form(self, form_class=None):
        form = super(CreatePost, self).get_form()
        form.fields["blog"].queryset = Blog.objects.all().filter(author=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)








