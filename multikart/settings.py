"""
Django settings for multikart project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import redis
from django.utils.translation import gettext_lazy as _
from datetime import timedelta



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


CELERY_TIMEZONE = 'Asia/Baku'


REDIS_BROKER_URL = 'redis://localhost:6379'

REDIS_CLIENT = redis.Redis.from_url(REDIS_BROKER_URL)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-90@7#^ah8)zrqurg!iny^3(-+$3j1x)s^gxxiiyarb3pn3lnk+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


AUTH_USER_MODEL = 'accounts.User'


# Application definition

INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_celery_beat',
    'drf_yasg',
    
    'order',
    'product',
    'user',
    'core',
    'accounts',
    'django_filters',
    'django_extensions',

]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    "TOKEN_OBTAIN_SERIALIZER": "accounts.api.serializers.CustomTokenObtainPairSerializer",
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,

    'JTI_CLAIM': 'jti',
}


MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'multikart.middleware.BlockIPMiddleware',
    'multikart.middleware.LogginMiddleware',

]

ROOT_URLCONF = 'multikart.urls'

# REST_FRAMEWORK = {
#      'DATETIME_FORMAT': "%m/%d/%Y %H:%M:%S",
#  }


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.custom_context_processor.subscriber_renderer',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '214846323822-p94mc29oo48el7evf2qvmdvf7gp3tslj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_FACEBOOK_KEY = '2015611941953131'   
SOCIAL_AUTH_FACEBOOK_SECRET = '27a1e6c0a45dc267be879e6fc9eab89a'

WSGI_APPLICATION = 'multikart.wsgi.application'



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '214846323822-p94mc29oo48el7evf2qvmdvf7gp3tslj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'multikart',
        'USER': 'user',
        'PASSWORD': '12345',
        'PORT': 5432,
        'HOST': 'localhost',
    }
}


# CELERY STUFF
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku' 


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/



LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('az', _('Azerbaijan')),
    ('en', _('English')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]



TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'


STATICFILES_DIRS = [
    BASE_DIR / 'static/'

]

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# JET_THEMES = [
#     {
#         'theme': 'default', # theme folder name
#         'color': '#47bac1', # color of the theme's button in user menu
#         'title': 'Default' # theme title
#     },
#     {
#         'theme': 'green',
#         'color': '#44b78b',
#         'title': 'Green'
#     },
#     {
#         'theme': 'light-green',
#         'color': '#2faa60',
#         'title': 'Light Green'
#     },
#     {
#         'theme': 'light-violet',
#         'color': '#a464c4',
#         'title': 'Light Violet'
#     },
#     {
#         'theme': 'light-blue',
#         'color': '#5EADDE',
#         'title': 'Light Blue'
#     },
#     {
#         'theme': 'light-gray',
#         'color': '#222',
#         'title': 'Light Gray'
#     }
# ]
AUTH_USER_MODEL = 'accounts.User'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mahammad.nabizade2@aiesec.net'
EMAIL_HOST_PASSWORD = 'IUYGILGA'
