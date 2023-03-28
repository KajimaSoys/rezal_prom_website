from django.apps import AppConfig


class RequestsConfig(AppConfig):
    verbose_name = 'Заявки от пользователей'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'requests'
