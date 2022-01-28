from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path("posts/", PostsView.as_view()),
    path("", IndexView.as_view()),
    path('post_create', PostCreateView.as_view(), name='post_create'),
    path('posts/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('post_delete/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),
    path('post_update/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
]