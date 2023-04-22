from django.db import models

class Order(models.Model):
    """
    Description of Order Model of Requests App
    """

    name = models.CharField(verbose_name='Имя', max_length=150)
    number = models.CharField(verbose_name='Номер телефона', max_length=40)
    message = models.TextField(verbose_name='Какая мебель нужна?', blank=True)
    comfortable_time = models.CharField(verbose_name='Удобное время', max_length=20, blank=True)

    project_version = models.CharField(verbose_name='Версия приложения', blank=True, max_length=10)
    created = models.DateTimeField(verbose_name='Создано', auto_now_add=True)

    user_agent = models.CharField(verbose_name='UserAgent', blank=True, max_length=2000)
    screen_resolution = models.CharField(verbose_name='Разрешение экрана', blank=True, max_length=100)
    browser_language = models.CharField(verbose_name='Язык браузера', blank=True, max_length=100)
    timezone = models.CharField(verbose_name='Временная зона', blank=True, max_length=100)
    cookie = models.TextField(verbose_name='Cookie', blank=True, max_length=5000)

    def __str__(self):
        return f'{self.name} - {self.message} - {self.created}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
