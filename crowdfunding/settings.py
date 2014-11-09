"""
Django settings for crowdfunding project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%fg2p6rq5v09pt+hc_4i7y+remwemt3lw&nyh7k1gx)14%jw^z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/project/'
#LOGIN_ERROR_URL    = '/login-error/'
FACEBOOK_APP_ID              = '1491007234499273'
FACEBOOK_API_SECRET          = '4d66a689da751a7d5eeef54381a16c23'

GOOGLE_OAUTH2_CLIENT_ID = '644166177318-3bcif9eb1k4oe18avmc2sucr0o3e61as.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'iQ4XxxHStUuz0iwO8UgQKuhP'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH = 128
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'google')
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'social.apps.django_app.default',
    'gunicorn',
    'south',
    'main',
    'auth',
    'project',
    'social_auth',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    # default context processors for Django 1.4
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # context processors for 'myproject'
    "crowdfunding.context_processors.baseurl",
    "social_auth.context_processors.social_auth_by_type_backends",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crowdfunding.urls'

WSGI_APPLICATION = 'crowdfunding.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crowdfunding',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Open Authentication procedures
# @documentation : http://psa.matiasaguirre.net/docs/index.html

AUTHENTICATION_BACKENDS = (
    # 'social.backends.open_id.OpenIdAuth',
    #  'social_auth.backends.google.GoogleOpenId',
    #  'social_auth.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    # 'social.backends.twitter.TwitterOAuth',
    # 'social.backends.yahoo.YahooOpenId',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend', # for django.contrib.auth username and password
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'sitestatic')

#MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'../media').replace('\\','/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'../media')


MEDIA_URL = "/media/"

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__),'static'),
    #'/opt/lakshya/Shakespeer/crowdfunding/static',
    os.path.join(BASE_DIR, 'crowdfunding/static')
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_DIRS = ('crowdfunding/templates',)

# Load the local settings
# This should be at the end for overriding
try:
     from .settings_local import *
except ImportError:
     print "You don't have a settings_local file"
     raise
