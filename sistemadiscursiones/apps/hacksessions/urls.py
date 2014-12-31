#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from .views import HacksessionsView, HackprivView, HackpubView, ProxHackView, calendario
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistemadiscursiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^hacksessions/$', HacksessionsView.as_view(), name='hacksessions'),
   url(r'^hack-priv/$', HackprivView.as_view(), name='hackpriv'),
   url(r'^hack-pub/$', HackpubView.as_view(), name='hackpub'),
   url(r'^proxhack/$', ProxHackView.as_view(), name='proxhack'),
   url(r'^calendario/$', 'apps.hacksessions.views.calendario', name='calendario'),
   
)