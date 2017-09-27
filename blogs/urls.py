# coding=utf-8
from django.conf.urls import url,include
from blogs.views import BlogList, BlogDetail, PostDetail, CreateBlog, UpdateBlog, CreatePost, UpdatePost, UpdateBlogDiv, UpdatePostDiv, \
LikeCountView, LikeView, CategoryView, PostLikeAjaxView, PostCommentDetail
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^newblog/',login_required(CreateBlog.as_view()), name="addblog"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="editblog"),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name="blogDetail"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(), name="postDetail"),

url(r'^ckeditor/', include('ckeditor_uploader.urls'), name="meow"),
    url(r'^newpost/',login_required(CreatePost.as_view()), name="addpost"),
    url(r'^posts/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="editpost"),
    url(r'^(?P<pk>\d+)/editdiv/$', login_required(UpdateBlogDiv.as_view()), name="editblogdiv"),
    url(r'^posts/(?P<pk>\d+)/editdiv/$', login_required(UpdatePostDiv.as_view()), name="editpostdiv"),
    url(r'^posts/(?P<pk>\d+)/likes/$', csrf_exempt(PostLikeAjaxView.as_view()), name="likecount"),
    url(r'posts/likes/$', LikeView.as_view(), name="likes"),
    url(r'^posts/(?P<pk>\d+)/comments/$', PostCommentDetail.as_view(), name="commentdiv"),


]


