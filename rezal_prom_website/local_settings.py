import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = 'django-insecure-x$^8ct)d^=g#9cd-!6tt$)k-8c9p(8zt+r6)4nt!ibtg&_@&x+'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",# from nginx in prod
    "http://localhost:5173",# from vite in dev
    "http://localhost:4173"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rezal_prom',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': 'D:/Programming/rezal_prom_website/cache'
#     }
# }

