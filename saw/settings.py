"""
Django settings for saw project.

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
SECRET_KEY = '$4&+-(j7ip2$pm)lq$jvw28l7o3sygc12r*fuk)6017l9ojcj6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (('stleon', 'leonst998@gmail.com'),)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'site_enter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'saw.urls'

WSGI_APPLICATION = 'saw.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CSRF_COOKIE_NAME = 'saw'

SESSION_COOKIE_NAME = 'saw'

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates')
)

STATIC_URL  ='/stuff/'

MEDIA_URL = '/another_stuff/'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'dynamic')

#STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static_content')