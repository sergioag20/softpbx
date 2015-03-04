# -*- coding: utf-8 -*-
#Coloque as configurações do seu database aqui
# Host, nome, portas etc...
# Não incluir este arquivo no git ...

__author__ = 'fchevitarese@gmail.com'
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'softpbx',
        'USER': 'root',
        'PASSWORD': 'ferrari',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cdr_tables',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

GRAPPELLI_ADMIN_TITLE = "SoftPbx"