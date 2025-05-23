"""
Django settings for AiShotServer project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-tt5bi*yhr$wn-snxpc=2s*_a%s(rc9u_j1@phs-^*pas%+hl8!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [# myproject/settings.py
'*'
]

APPEND_SLASH=False

# Application definition

INSTALLED_APPS = [
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework_simplejwt',
    'corsheaders',
    "AiShotServer",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "AiShotServer.middleware.MyAuthenticationMiddleware.MyAuthenticationMiddleware"
]

ROOT_URLCONF = "AiShotServer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "AiShotServer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "t/"
STATICFILES_DIRS = [
    BASE_DIR / "AiShotServer/static",
    'AiShotServer/t',
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # 使用JWT认证
    ],
   """  'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # 需要认证才能访问API
    ], """ ##TODO ,use to test api
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # 返回JSON格式的响应
    ],
    'EXCEPTION_HANDLER': 'AiShotServer.util.custom_exception_handler',
}


APPEND_SLASH = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 不禁用已有的日志记录器
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',  # 输出到控制台,
            'level':'DEBUG',
            'formatter': 'verbose',  # 使用verbose格式
        },
        'file': {
            'level': 'DEBUG',  # 设置文件日志记录级别
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_debug.log'),  # 日志文件路径
            'formatter': 'verbose',  # 使用verbose格式
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console' ],  # 处理器
            'level': 'WARNING',  # 设置Django日志级别为DEBUG
            'propagate': False,  # 传播日志
        },
        # 可以添加其他的logger
        'AiShotServer': {  # 替换为你的应用名称
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rest_framework': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },

    },
}
 
 
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),  # 默认是 5 分钟
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),  # 默认是 1 天
}

AUTH_USER_MODEL = 'AiShotServer.customuser'
DEBUG = True