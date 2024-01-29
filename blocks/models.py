from django.db import models
from ckeditor.fields import RichTextField


class HeaderBlock(models.Model):
    """
    Description of HeaderBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Навигационная панель'
        verbose_name_plural = 'Навигационная панель'

    logo = models.FileField(verbose_name='Лого', upload_to='header/', max_length=500)

    address = models.CharField(verbose_name='Адрес компании', max_length=255, default='')
    yandex_map_link = models.CharField(verbose_name='Ссылка на Яндекс Карты', max_length=500, default='')
    schedule = models.CharField(verbose_name='Расписание', max_length=255, default='')
    number = models.CharField(verbose_name='Номер компании', max_length=18)

    tg_link = models.CharField(verbose_name='Ссылка на Telegram', max_length=255, default='', blank=True)
    whatsapp_link = models.CharField(verbose_name='Ссылка на Whatsapp', max_length=255, default='', blank=True)
    instagram_link = models.CharField(verbose_name='Ссылка на Instagram', max_length=255, default='', blank=True)
    vk_link = models.CharField(verbose_name='Ссылка на VK', max_length=255, default='', blank=True)

    def __str__(self):
        return 'Навигационная панель'


class MainBlock(models.Model):
    """
    Description of MainBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Главный блок'
        verbose_name_plural = 'Главный блок'

    title = RichTextField(verbose_name='Заголовок блока')
    description = RichTextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='main/', max_length=500)

    def __str__(self):
        return 'Главный блок'


class AboutBlock(models.Model):
    """
    Description of AboutBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок о компании'
        verbose_name_plural = 'Блок о компании'

    title = RichTextField(verbose_name='Заголовок блока', blank=True)
    description = RichTextField(verbose_name='Описание')

    title_first = RichTextField(verbose_name='Заголовок №1')
    description_first = RichTextField(verbose_name='Описание №1')

    title_second = RichTextField(verbose_name='Заголовок №2')
    description_second = RichTextField(verbose_name='Описание №2')

    title_third = RichTextField(verbose_name='Заголовок №3')
    description_third = RichTextField(verbose_name='Описание №3')

    title_fourth = RichTextField(verbose_name='Заголовок №4')
    description_fourth = RichTextField(verbose_name='Описание №4')

    title_fifth = RichTextField(verbose_name='Заголовок №5')
    description_fifth = RichTextField(verbose_name='Описание №5')

    title_sixth = RichTextField(verbose_name='Заголовок №6')
    description_sixth = RichTextField(verbose_name='Описание №6')

    def __str__(self):
        return 'Блок о компании'


class ProductionBlock(models.Model):
    """
    Description of ProductionBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок производства'
        verbose_name_plural = 'Блок производства'

    title = RichTextField(verbose_name='Заголовок блока')
    description = RichTextField(verbose_name='Описание')

    video_preview = models.ImageField(verbose_name='Превью для видео', upload_to='warming/', max_length=500)
    video_link = models.CharField(verbose_name='Ссылка на видео', blank=True, max_length=500)

    image_one = models.ImageField(verbose_name='Фото №1', upload_to='warming/', max_length=500)
    image_two = models.ImageField(verbose_name='Фото №2', upload_to='warming/', max_length=500)
    image_three = models.ImageField(verbose_name='Фото №3', upload_to='warming/', max_length=500)

    def __str__(self):
        return 'Блок производства'


class ServicesBlock(models.Model):
    """
    Description of ServicesBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок услуг'
        verbose_name_plural = 'Блок услуг'

    title = RichTextField(verbose_name='Заголовок блока')

    title_first = RichTextField(verbose_name='Заголовок №1')
    title_second = RichTextField(verbose_name='Заголовок №2')
    title_third = RichTextField(verbose_name='Заголовок №3')

    def __str__(self):
        return 'Блок услуг'


class ProjectsBlock(models.Model):
    """
    Description of ProjectsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок проектов'
        verbose_name_plural = 'Блок проектов'

    title = RichTextField(verbose_name='Заголовок блока')

    title_first = RichTextField(verbose_name='Заголовок №1')
    description_first = RichTextField(verbose_name='Описание №1')
    image_first = models.ImageField(verbose_name='Фото №1', upload_to='projects/', max_length=500)
    video_link_first = models.CharField(verbose_name='Ссылка на видео №1', max_length=500, blank=True)

    title_second = RichTextField(verbose_name='Заголовок №2')
    description_second = RichTextField(verbose_name='Описание №2')
    image_second = models.ImageField(verbose_name='Фото №2', upload_to='projects/', max_length=500)
    video_link_second = models.CharField(verbose_name='Ссылка на видео №2', max_length=500, blank=True)

    title_third = RichTextField(verbose_name='Заголовок №3')
    description_third = RichTextField(verbose_name='Описание №3')
    image_third = models.ImageField(verbose_name='Фото №3', upload_to='projects/', max_length=500)
    video_link_third = models.CharField(verbose_name='Ссылка на видео №3', max_length=500, blank=True)

    # title_forth = RichTextField(verbose_name='Заголовок №4')
    # image_forth = models.ImageField(verbose_name='Фото №4', upload_to='projects/', max_length=500)
    # video_link_forth = models.CharField(verbose_name='Ссылка на видео №4', max_length=500)

    def __str__(self):
        return 'Блок проектов'


class StagesBlock(models.Model):
    """
    Description of StagesBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок стадий работ'
        verbose_name_plural = 'Блок стадий работ'

    title = RichTextField(verbose_name='Заголовок блока')

    # title_first = RichTextField(verbose_name='Текст №1')
    # image_first = models.ImageField(verbose_name='Фото №1', upload_to='stages/', max_length=500)
    #
    # title_second = RichTextField(verbose_name='Текст №2')
    # image_second = models.ImageField(verbose_name='Фото №2', upload_to='stages/', max_length=500)
    #
    # title_third = RichTextField(verbose_name='Текст №3')
    # image_third = models.ImageField(verbose_name='Фото №3', upload_to='stages/', max_length=500)
    #
    # title_fourth = RichTextField(verbose_name='Текст №4')
    # image_fourth = models.ImageField(verbose_name='Фото №4', upload_to='stages/', max_length=500)
    #
    # title_fifth = RichTextField(verbose_name='Текст №5')
    # image_fifth = models.ImageField(verbose_name='Фото №5', upload_to='stages/', max_length=500)
    #
    # title_sixth = RichTextField(verbose_name='Текст №6')
    # image_sixth = models.ImageField(verbose_name='Фото №6', upload_to='stages/', max_length=500)
    #
    # title_seventh = RichTextField(verbose_name='Текст №7')
    # image_seventh = models.ImageField(verbose_name='Фото №7', upload_to='stages/', max_length=500)
    #
    # title_eighth = RichTextField(verbose_name='Текст №8')
    # image_eighth = models.ImageField(verbose_name='Фото №8', upload_to='stages/', max_length=500)

    delivery_title = RichTextField(verbose_name='Заголовок доставки')

    delivery_first = RichTextField(verbose_name='Доставка №1')

    delivery_second = RichTextField(verbose_name='Доставка №2')

    def __str__(self):
        return 'Блок стадий работ'


class TeamBlock(models.Model):
    """
    Description of TeamBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок команды'
        verbose_name_plural = 'Блок команды'

    title = RichTextField(verbose_name='Заголовок блока')
    description = RichTextField(verbose_name='Описание')

    # first_name = RichTextField(verbose_name='Имя первого человека')
    # first_post = RichTextField(verbose_name='Должность первого человека')
    # first_image = models.ImageField(verbose_name='Фото первого человека', upload_to='team/', max_length=500)
    #
    # second_name = RichTextField(verbose_name='Имя второго человека')
    # second_post = RichTextField(verbose_name='Должность второго человека')
    # second_image = models.ImageField(verbose_name='Фото второго человека', upload_to='team/', max_length=500)

    def __str__(self):
        return 'Блок команды'


class QuestionsBlock(models.Model):
    """
    Description of QuestionsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок часто задаваемых вопросов'
        verbose_name_plural = 'Блок часто задаваемых вопросов'

    title = RichTextField(verbose_name='Заголовок блока')

    # question_first = RichTextField(verbose_name='Вопрос №1')
    # answer_first = RichTextField(verbose_name='Ответ №1')
    #
    # question_second = RichTextField(verbose_name='Вопрос №2')
    # answer_second = RichTextField(verbose_name='Ответ №2')
    #
    # question_third = RichTextField(verbose_name='Вопрос №3')
    # answer_third = RichTextField(verbose_name='Ответ №3')
    #
    # question_fourth = RichTextField(verbose_name='Вопрос №4')
    # answer_fourth = RichTextField(verbose_name='Ответ №4')
    #
    # question_fifth = RichTextField(verbose_name='Вопрос №5')
    # answer_fifth = RichTextField(verbose_name='Ответ №5')

    def __str__(self):
        return 'Блок часто задаваемых вопросов'


class ReviewsBlock(models.Model):
    """
    Description of ReviewsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок отзывов клиентов'
        verbose_name_plural = 'Блок отзывов клиентов'

    title = RichTextField(verbose_name='Заголовок блока')

    def __str__(self):
        return 'Блок отзывов клиентов'


class ContactsBlock(models.Model):
    """
    Description of ContactsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок контактов'
        verbose_name_plural = 'Блок контактов'

    title = RichTextField(verbose_name='Заголовок блока')

    address = models.CharField(verbose_name='Адрес компании', max_length=255, default='')
    yandex_map_link = models.CharField(verbose_name='Ссылка на Яндекс Карты', max_length=500, default='')
    schedule = models.CharField(verbose_name='Расписание', max_length=255, default='')
    number = models.CharField(verbose_name='Номер компании', max_length=18)

    instagram_link = models.CharField(verbose_name='Ссылка на Instagram', max_length=255, default='')
    vk_link = models.CharField(verbose_name='Ссылка на VK', max_length=255, default='')

    def __str__(self):
        return 'Блок контактов'
