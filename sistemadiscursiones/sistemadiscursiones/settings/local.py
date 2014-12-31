#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-*-encoding: utf-8 -*-
from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'discursiones',
        'USER': 'cursodjango',
        'PASSWORD' : 'pass',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '304132099753397'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c7b34691dcc102f284c6f05cbb8a18ad'

SOCIAL_AUTH_TWITTER_KEY = 'TG014isV1sltVDxePLPOMFZlR'
SOCIAL_AUTH_TWITTER_SECRET = 'x565TuKBAU1qGcfDiAB0ArSgEf2dzVYuIrmwF3J8OPX28keEht'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "398802098425-jqih89289rns6jsptgq57d5m6cutt971.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "s8cEmAupsV_-WsODFdXgAl80"


EMAIL_HOST = 'hackingcodeschool.net'
EMAIL_HOST_USER = 'ada_lovelance@hackingcodeschool.net'
EMAIL_HOST_PASSWORD = 'pass'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'hackingcodeschool.net'
