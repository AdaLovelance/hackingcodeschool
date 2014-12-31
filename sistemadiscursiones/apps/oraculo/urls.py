from django.conf.urls import patterns, include, url
from .views import OraculoList
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

	   url(r'^oraculolist/$', OraculoList.as_view() , name='oraculolist'),

	 )