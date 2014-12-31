#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistemadiscursiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.users.urls', namespace='users')),
    url(r'^', include('apps.oraculo.urls',)),
    url(r'^', include('apps.discuss.urls', namespace = 'discuss')),
    url(r'^', include('apps.hacksessions.urls',)),
    url(r'^', include('apps.biblioteca.urls',)),
    url(r'^', include('apps.servicios.urls',)),
    url(r'^', include('apps.contacto.urls',)),
    #url(r'^', include('apps.blog.urls',)),
    #url(r'^', include('apps.foro.urls',)),
    #url(r'^', include('apps.cursos.urls',)),
    url(r'^admin/', include(admin.site.urls)),
    #python social auth
    #url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('social_auth.urls')),
    (r'^foro/', include('pybb.urls', namespace='pybb')),

   
)
