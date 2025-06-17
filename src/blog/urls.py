from django.contrib import admin
from django.urls import path
from django.views.defaults import server_error

from .views import index, article

urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<str:article_id>/', article, name="blog-article"),
]