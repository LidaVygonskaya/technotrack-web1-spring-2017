# coding=utf-8
from django.conf.urls import url, include
from blogs.views import BlogList, BlogDetail, PostDetail, CreateBlog, UpdateBlog, CreatePost, UpdatePost
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^newblog/',login_required(CreateBlog.as_view()), name="addblog"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="editblog"),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name="blogDetail"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(), name="postDetail"),
    url(r'^newpost/',login_required(CreatePost.as_view()), name="addpost"),
    url(r'^posts/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="editpost"),

]

