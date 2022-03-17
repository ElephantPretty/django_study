"""
Django settings for django_admin project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 项目绝对路径
BASE_DIR = Path(__file__).resolve().parent.parent
# print(Path(__file__))
# print(Path(__file__).resolve().parent)
# print(Path(__file__).resolve().parent.parent)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z4g_0u_nkk_)6ds3d7ow6p7&9zhrjcj%t4$a*g=$_ve1mzw1pi'

# SECURITY WARNING: don't run with debug turned on in production!
# 启动模式 True-调试模式 False-正式启动模式/上线模式
"""
DEBUG--启动模式 True-调试模式 False-正式启动模式/上线模式
True
1--检测代码改动后，立刻重启服务
2--报错页面
False
正式启动模式/上线模式
"""
DEBUG = True

# 请求头Host值
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # session配置1
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 自定义应用名--模版的路由规则
    'music',
    'sport',
    'news',
    # 模型测试
    'bookstore',
    'oto',
    'otm',
    'mtm'
]
#和静态文件相关，默认会配置

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # session配置2
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # post请求时会有一个csrf防范
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 2.0.12需要自己加，但是4版本是配置好了的
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        # 这个配置代表应用内部是否要使用模板，true代表开启
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

WSGI_APPLICATION = 'django_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        # mysql配置
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_admin',
        'USER':'root',
        'PASSWORD':'1040994588',
        'HOST':'120.24.191.123',
        'PORT':'3306'
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# 时区 语言
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
"""
类似于访问静态文件的令牌
如果你想访问静态文件，你就必须以static开头
"""
STATIC_URL = 'static/'

# # 一个元素的元组一定是需要有逗号的
# STATICFILES_DIRS = [
#     # os.path.join(BASE_DIR, 'static/')
#     BASE_DIR/'static'
# ]
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
