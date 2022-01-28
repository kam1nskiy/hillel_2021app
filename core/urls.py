from django.urls import path
from .views import PostsView
from .views import IndexView

urlpatterns = [
    path("posts/",PostsView.as_view()),
    path("", IndexView.as_view()),

    ]