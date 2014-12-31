from django.conf.urls import patterns, include, url
from .views import ServiciosView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistemadiscursiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^servicios/$', ServiciosView.as_view(), name='servicios'),


   )