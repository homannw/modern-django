from .base import *


DEBUG = env.bool('DJANGO_DEBUG', True)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='c^hp6=(ice!b0jx(r*e+-%dmbl&@=2xk18ii%*q3(g(8-ovudo')

