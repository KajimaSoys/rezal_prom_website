import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = (os.environ.get('DEBUG') == 'True')
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get("ALLOWED_HOSTS", "").split(","),
    )
)

CSRF_TRUSTED_ORIGINS = [os.environ.get("CSRF_TRUSTED")]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",  # from nginx in prod
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

CSRF_COOKIE_SECURE = (os.environ.get('CSRF_COOKIE_SECURE', False) == 'True')
SESSION_COOKIE_SECURE = (os.environ.get('SESSION_COOKIE_SECURE', False) == 'True')

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/home/kajimasoys/website/cache'
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
