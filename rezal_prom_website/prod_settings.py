import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = (os.environ.get('REZAL_PROM_DEBUG') == 'True')
ALLOWED_HOSTS = os.environ.get('REZAL_PROM_ALLOWED_HOSTS', '127.0.0.1').split(',')
SECRET_KEY = os.environ.get('REZAL_PROM_SECRET_KEY')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",# from nginx in prod
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('REZAL_PROM_POSTGRES_NAME'),
        'USER': os.environ.get('REZAL_PROM_POSTGRES_USER'),
        'PASSWORD': os.environ.get('REZAL_PROM_POSTGRES_PASSWORD'),
        'HOST': os.environ.get('REZAL_PROM_POSTGRES_HOST'),
        'PORT': os.environ.get('REZAL_PROM_POSTGRES_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

CSRF_COOKIE_SECURE = (os.environ.get('REZAL_PROM_CSRF_COOKIE_SECURE', False) == 'True')
SESSION_COOKIE_SECURE = (os.environ.get('REZAL_PROM_SESSION_COOKIE_SECURE', False) == 'True')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/kajimasoys/rezal_prom_website/cache'
    }
}
