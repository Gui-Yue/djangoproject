from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^titles/$', views.titles, name='titles'),
    url(r'^titles/(?P<title_id>\d+)/$', views.title, name='title'),
    url(r'^new_title/$', views.new_title, name='new_title'),
    url(r'^new_content/(?P<title_id>\d+)/$', views.new_content, name='new_content'),
    url(r'^edit_content/(?P<content_id>\d+)/$', views.edit_content, name='edit_content'),
]