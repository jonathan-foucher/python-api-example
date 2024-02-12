"""
Django settings for djangoapp project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fynw3whn#ljns$q#^t2sou1a-h$l-b7dcqywfz19-8_c(lx#_6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'apps.player',
]

ROOT_URLCONF = 'djangoapp.urls'

WSGI_APPLICATION = 'djangoapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "django",
        'USER': "django",
        'PASSWORD': "django",
        'HOST': "localhost",
        'PORT': "5432",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

TIME_ZONE = 'UTC'

USE_TZ = True

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        'rest_framework.renderers.JSONRenderer',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "UNAUTHENTICATED_USER": None,
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter'
    ],
}