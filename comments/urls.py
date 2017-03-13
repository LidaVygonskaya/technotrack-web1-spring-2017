from django.conf.urls import url, include

from comments.views import CommentDetail

urlpatterns = [
    url(r'^(?P<comment_id>\d+)/$', CommentDetail.as_view(), name='commentDetails'),
]