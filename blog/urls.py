from django.urls import path
from . import views
urlpatterns = [
    path(r'^article_list/$', views.article_list, name='article_list'),
    path(r'', views.blog_base, name='blog_base'),
]