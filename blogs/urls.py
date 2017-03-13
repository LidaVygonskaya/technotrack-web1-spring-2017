# coding=utf-8
from django.conf.urls import url, include
from blogs.views import BlogList, BlogDetail, PostDetail

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<blog_id>\d+)/$', BlogDetail.as_view(), name="blogDetail"),
    url(r'^(?P<blog_id>\d+)/(?P<post_id>\d+)/$', PostDetail.as_view(), name="postDetail"),
    url(r'^(?P<blog_id>\d+)/(?P<post_id>\d+)/', include('comments.urls',namespace="comments"))

]

