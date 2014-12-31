from django.conf.urls import patterns, include, url
from .views import ContactoView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistemadiscursiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^contacto/$', ContactoView.as_view(), name='contacto'),


   )