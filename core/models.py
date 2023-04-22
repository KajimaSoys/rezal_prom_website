from django.db import models
from ckeditor.fields import RichTextField


class Stages(models.Model):
    """
    Description of Stages Model of Core App
    """

    class Meta:
        verbose_name = 'этап работ'
        verbose_name_plural = 'этапы работ'
        ordering = ['order']

    title = RichTextField(verbose_name='Текст этапа')
    image = models.ImageField(verbose_name='Фото этапа', upload_to='stages/', max_length=500)

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title


class Staff(models.Model):
    """
    Description of Staff Model of Core App
    """

    class Meta:
        verbose_name = 'персонал'
        verbose_name_plural = 'персонал'
        ordering = ['order']

    name = RichTextField(verbose_name='Имя')
    post = RichTextField(verbose_name='Должность')
    image = models.ImageField(verbose_name='Фото', upload_to='team/', max_length=500)

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class Questions(models.Model):
    """
    Description of Questions Model of Core App
    """

    class Meta:
        verbose_name = 'часто задаваемый вопрос'
        verbose_name_plural = 'часто задаваемые вопросы'
        ordering = ['order']

    question = RichTextField(verbose_name='Вопрос')
    answer = RichTextField(verbose_name='Ответ')

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.question


class ReviewText(models.Model):
    """
    Description of ReviewText Model of Core App
    """

    class Meta:
        verbose_name = 'текcтовый отзыв'
        verbose_name_plural = 'текcтовые отзывы'
        ordering = ['order']

    author_name = RichTextField(verbose_name='Имя автора отзыва')
    review_text = RichTextField(verbose_name='Текст отзыва')
    author_photo = models.ImageField(verbose_name='Фото автора отзыва', upload_to='authors/', blank=True)
    review_link = models.CharField(verbose_name='Ссылка на отзыв', max_length=1000, blank=True)

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.author_name


class ReviewVideo(models.Model):
    """
    Description of ReviewVideo Model of Core App
    """

    class Meta:
        verbose_name = 'видео отзыв'
        verbose_name_plural = 'видео отзывы'
        ordering = ['order']

    image = models.ImageField(verbose_name='Превью отзыва', upload_to='projects/', max_length=500)
    video_link = models.CharField(verbose_name='Ссылка на видео отзыв', max_length=1000)

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'Отзыв №{self.id}'
