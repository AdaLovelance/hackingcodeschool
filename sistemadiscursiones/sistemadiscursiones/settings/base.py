#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)


SECRET_KEY = 'h7&rg-3rrm3l&deq4fvsddd=1zag927y2uvpkvi=rpr^hr!)i4'


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
 )

TRIRD_PARTY_APPS = (
    'south',
    'social.apps.django_app.default',
    'pybb',
    
    
    )

LOCAL_APPS = (
    'apps.home',
    'apps.users',
    'apps.hacksessions',
    'apps.oraculo',
    'apps.discuss',
    'apps.biblioteca',
    'apps.servicios',
    'apps.contacto',
    'apps.blog',
    'apps.cursos',
    


    )


INSTALLED_APPS = DJANGO_APPS + TRIRD_PARTY_APPS + LOCAL_APPS                

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'sistemadiscursiones.urls'

WSGI_APPLICATION = 'sistemadiscursiones.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.google.GoogleOAuth2',
    'social_auth.backends.contrib.github.GithubBackend',
    'apps.users.backends.EmailAuthentication',
    
    )

LOGIN_URL          = '/login/'

LOGIN_ERROR_URL    = '/error/'
LOGIN_REDIRECT_URL = '/'
#SOCIAL_AUTH_LOGIN_URL = '/error/'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SOCIAL_AUTH_USERNAME_FORM_URL = '/login-form/'

#AUTH_USER_MODEL = 'users.User'
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',

    'apps.users.pipelines.get_avatar',
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'

    )


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    # Django default context processors
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
    'pybb.context_processors.processor',  

    )

# Requerido por django.contrib.sites
SITE_ID = 3

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'SCOPE': ['email', 'user_likes', 'user_status', 'user_about_me', 'read_stream'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False}}


 
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

SOUTH_MIGRATION_MODULES = {
    'pybb': 'pybb.south_migrations',
}
