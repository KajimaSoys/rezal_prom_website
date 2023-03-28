from django.db import models

class HeaderBlock(models.Model):
    """
    Description of HeaderBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Навигационная панель'
        verbose_name_plural = 'Навигационная панель'

    logo = models.ImageField(verbose_name='Лого', upload_to='header/', max_length=500)
    number = models.CharField(verbose_name='Номер компании', max_length=15)

    def __str__(self):
        return 'Навигационная панель'


class MainBlock(models.Model):
    """
    Description of MainBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Главный блок'
        verbose_name_plural = 'Главный блок'

    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
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

    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    title_first = models.TextField(verbose_name='Заголовок №1')
    description_first = models.TextField(verbose_name='Описание №1')

    title_second = models.TextField(verbose_name='Заголовок №2')
    description_second = models.TextField(verbose_name='Описание №2')

    title_third = models.TextField(verbose_name='Заголовок №3')
    description_third = models.TextField(verbose_name='Описание №3')

    title_fourth = models.TextField(verbose_name='Заголовок №4')
    description_fourth = models.TextField(verbose_name='Описание №4')

    title_fifth = models.TextField(verbose_name='Заголовок №5')
    description_fifth = models.TextField(verbose_name='Описание №5')

    title_sixth = models.TextField(verbose_name='Заголовок №6')
    description_sixth = models.TextField(verbose_name='Описание №6')

    def __str__(self):
        return 'Блок о компании'


class WarmingBlock(models.Model):
    """
    Description of WarmingBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок прогрева'
        verbose_name_plural = 'Блок прогрева'

    image = models.ImageField(verbose_name='Фото', upload_to='warming/', max_length=500)
    title = models.TextField(verbose_name='Заголовок')

    def __str__(self):
        return 'Блок прогрева'


class ServicesBlock(models.Model):
    """
    Description of ServicesBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок услуг'
        verbose_name_plural = 'Блок услуг'

    title_first = models.TextField(verbose_name='Заголовок №1')
    image_first = models.ImageField(verbose_name='Фото №1', upload_to='service/', max_length=500)

    title_second = models.TextField(verbose_name='Заголовок №2')
    image_second = models.ImageField(verbose_name='Фото №2', upload_to='service/', max_length=500)

    title_third = models.TextField(verbose_name='Заголовок №3')
    image_third = models.ImageField(verbose_name='Фото №3', upload_to='service/', max_length=500)

    def __str__(self):
        return 'Блок услуг'


class ProjectsBlock(models.Model):
    """
    Description of ProjectsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок проектов'
        verbose_name_plural = 'Блок проектов'

    title_first = models.TextField(verbose_name='Заголовок №1')
    image_first = models.ImageField(verbose_name='Фото №1', upload_to='projects/', max_length=500)
    video_link_first = models.CharField(verbose_name='Ссылка на видео №1', max_length=500)

    title_second = models.TextField(verbose_name='Заголовок №2')
    image_second = models.ImageField(verbose_name='Фото №2', upload_to='projects/', max_length=500)
    video_link_second = models.CharField(verbose_name='Ссылка на видео №2', max_length=500)

    title_third = models.TextField(verbose_name='Заголовок №3')
    image_third = models.ImageField(verbose_name='Фото №3', upload_to='projects/', max_length=500)
    video_link_third = models.CharField(verbose_name='Ссылка на видео №3', max_length=500)

    title_forth = models.TextField(verbose_name='Заголовок №4')
    image_forth = models.ImageField(verbose_name='Фото №4', upload_to='projects/', max_length=500)
    video_link_forth = models.CharField(verbose_name='Ссылка на видео №4', max_length=500)

    def __str__(self):
        return 'Блок проектов'


class StagesBlock(models.Model):
    """
    Description of StagesBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок стадий работ'
        verbose_name_plural = 'Блок стадий работ'

    title_first = models.TextField(verbose_name='Текст №1')

    title_second = models.TextField(verbose_name='Текст №2')

    title_third = models.TextField(verbose_name='Текст №3')

    title_fourth = models.TextField(verbose_name='Текст №4')

    title_fifth = models.TextField(verbose_name='Текст №5')

    title_sixth = models.TextField(verbose_name='Текст №6')

    title_seventh = models.TextField(verbose_name='Текст №7')

    title_eighth = models.TextField(verbose_name='Текст №8')

    title_ninth = models.TextField(verbose_name='Текст №9')

    delivery_first = models.TextField(verbose_name='Доставка №1')

    delivery_second = models.TextField(verbose_name='Доставка №2')

    def __str__(self):
        return 'Блок стадий работ'


class TeamBlock(models.Model):
    """
    Description of TeamBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок команды'
        verbose_name_plural = 'Блок команды'

    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    image_director = models.ImageField(verbose_name='Фото владельца', upload_to='team/', max_length=500)
    image_manager = models.ImageField(verbose_name='Фото управляющего', upload_to='team/', max_length=500)

    def __str__(self):
        return 'Блок команды'


class QuestionsBlock(models.Model):
    """
    Description of QuestionsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок часто задаваемых вопросов'
        verbose_name_plural = 'Блок часто задаваемых вопросов'

    question_first = models.TextField(verbose_name='Вопрос №1')
    answer_first = models.TextField(verbose_name='Ответ №1')

    question_second = models.TextField(verbose_name='Вопрос №2')
    answer_second = models.TextField(verbose_name='Ответ №2')

    question_third = models.TextField(verbose_name='Вопрос №3')
    answer_third = models.TextField(verbose_name='Ответ №3')

    question_fourth = models.TextField(verbose_name='Вопрос №45')
    answer_fourth = models.TextField(verbose_name='Ответ №45')

    question_fifth = models.TextField(verbose_name='Вопрос №5')
    answer_fifth = models.TextField(verbose_name='Ответ №5')



    def __str__(self):
        return 'Блок часто задаваемых вопросов'


class ReviewsBlock(models.Model):
    """
    Description of ReviewsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок отзывов клиентов'
        verbose_name_plural = 'Блок отзывов клиентов'

    # fields

    def __str__(self):
        return 'Блок отзывов клиентов'


class ContactsBlock(models.Model):
    """
    Description of ContactsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок контактов'
        verbose_name_plural = 'Блок контактов'

    address = models.TextField(verbose_name='Адрес')
    schedule = models.TextField(verbose_name='Расписание')
    number = models.TextField(verbose_name='Номер')
    vk_link = models.TextField(verbose_name='Ссылка на вк')

    def __str__(self):
        return 'Блок контактов'


class FooterBlock(models.Model):
    """
    Description of FooterBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок футера'
        verbose_name_plural = 'Блок футера'

    logo = models.ImageField(verbose_name='Лого', upload_to='footer/', max_length=500)
    number = models.CharField(verbose_name='Номер компании', max_length=15)

    def __str__(self):
        return 'Блок футера'


