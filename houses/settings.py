"""
Django settings for houses project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from rest_framework.settings import api_settings
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tsw(828+vh_(t2#8%yfly3sk1#k#%1m81pu6^cbzy)c3ia%v+&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Whitelisting React Port (allowed ports to host the react application)

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [

    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Application definition

INSTALLED_APPS = [
    
    # System Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    
    #Third party apps
    'knox',
    'mpesa',
    
    # Main app
    'accounts',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'houses.urls'

REST_FRAMEWORK = {
    # DEFAULT AUTHENTICATION CLASSES
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
        
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    
    'PAGE_SIZE': 10,
    
    # PERMISSION CLASSES
    'DEFAULT_PERMISSION_CLASSES' : ('rest_framework.permissions.IsAuthenticated',),
    
    'DEFAULT_FILTER_BACKENDS': (        
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
),
    'DATETIME_FORMAT': '%d/%m/%Y %H:%M:%S',
}

# REST AUTH SERIALIZERS
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer'
}

# REST AUTH REGISTER SERIALIZERS
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': (
        'accounts.serializers.OwnerRegisterSerializer',
        'accounts.serializers.TenantRegisterSerializer'
        )
}

# REST KNOX SETTINGS
REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64, # By default, it is set to 64 characters(this shouldn't need changing).
    'USER_SERIALIZER': 'accounts.serializers.UserSerializer',
    'TOKEN_TTL': timedelta(minutes=45), # The default is 10 hours, i.e. timedelta(hours=10).
    'TOKEN_LIMIT_PER_USER': None,
    'AUTO_REFRESH': False, # This defines if the token expiry time is extended by TOKEN_TTL each times the token is used.
    'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT
}


TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'houses.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST':'127.0.0.1',
        'USER':'postgres',
        'PORT':'5432',
        'NAME': 'houses',
        'PASSWORD':'newdream'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'img')

STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'build/static')
]

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Default Custom User Account
AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_UNIQUE_EMAIL = True