# -*- coding: utf-8 -*-
# Coloque as configurações do seu database aqui
# Host, nome, portas etc...
# Não incluir este arquivo no git ...
import os

__author__ = 'fchevitarese@gmail.com'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'spw_softpbx',
        'USER': 'root',
        'PASSWORD': 'ferrari',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spw_extension',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
