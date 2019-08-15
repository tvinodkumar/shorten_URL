from django.conf.urls import url
from django.contrib import admin
from .views import Shorten_URLs_API_Class
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'post_shorten_url', Shorten_URLs_API_Class.as_view()),
    url(r'get_shorten_url', Shorten_URLs_API_Class.as_view()),
    url(r'create_shorten_url', views.create_shorten_url),
    url(r'insert_shorten_url', views.shorten_URL_View),
    url(r'list_shorten_url', views.list_shorten_url),
]
