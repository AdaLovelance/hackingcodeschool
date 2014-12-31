#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from .views import ExtraDataView, UserDetailView, UserProfileEditView

urlpatterns = patterns('',
   url(r'^log-out/$', 'apps.users.views.LogOut', name='logout'),
   url(r'^extra-data/$', ExtraDataView.as_view(), name='extra-data'),
   url(r'^usuario/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='user_detail'),
   url(r'^registro/$', "apps.users.views.login_Registro", name='registro'),
   url(r'^login/$', 'apps.users.views.login_User', name='login'),
   url(r'^perfil/$', auth(UserProfileEditView.as_view()), name="perfil"),
   url(r'^logueo/$', 'apps.users.views.logueo', name='logueo'),
)