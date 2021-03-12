# -*- coding: utf-8 -*-
from .base import *

SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  False

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = "strict-origin"
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
PREPEND_WWW = True
BASE_URL = "http://machtili.com.mx"

ALLOWED_HOSTS = ['www.machtili.com.mx', 'machtili.com.mx','localhost','127.0.0.1']
