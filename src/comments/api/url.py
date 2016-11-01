from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentListAPIView,
    CommentsDetailAPIView,
    CommentCreateAPIView,


    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CommentsDetailAPIView.as_view(), name='thread'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),

   # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]

