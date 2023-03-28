from django.db import models

class HeaderBlock(models.Model):
    """
    Description of HeaderBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Навигационная панель'
        verbose_name_plural = 'Навигационная панель'

    # fields

    def __str__(self):
        return 'Навигационная панель'


class MainBlock(models.Model):
    """
    Description of MainBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Главный блок'
        verbose_name_plural = 'Главный блок'

    # fields

    def __str__(self):
        return 'Главный блок'


class AboutBlock(models.Model):
    """
    Description of AboutBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок о компании'
        verbose_name_plural = 'Блок о компании'

    # fields

    def __str__(self):
        return 'Блок о компании'


class WarmingBlock(models.Model):
    """
    Description of WarmingBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок прогрева'
        verbose_name_plural = 'Блок прогрева'

    # fields

    def __str__(self):
        return 'Блок прогрева'


class ServicesBlock(models.Model):
    """
    Description of ServicesBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок услуг'
        verbose_name_plural = 'Блок услуг'

    # fields

    def __str__(self):
        return 'Блок услуг'


class ProjectsBlock(models.Model):
    """
    Description of ProjectsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок проектов'
        verbose_name_plural = 'Блок проектов'

    # fields

    def __str__(self):
        return 'Блок проектов'


class StagesBlock(models.Model):
    """
    Description of StagesBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок стадий работ'
        verbose_name_plural = 'Блок стадий работ'

    # fields

    def __str__(self):
        return 'Блок стадий работ'


class TeamBlock(models.Model):
    """
    Description of TeamBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок команды'
        verbose_name_plural = 'Блок команды'

    # fields

    def __str__(self):
        return 'Блок команды'


class QuestionsBlock(models.Model):
    """
    Description of QuestionsBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок часто задаваемых вопросов'
        verbose_name_plural = 'Блок часто задаваемых вопросов'

    # fields

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

    # fields

    def __str__(self):
        return 'Блок контактов'


class FooterBlock(models.Model):
    """
    Description of FooterBlock Model of Blocks App
    """
    class Meta:
        verbose_name = 'Блок футера'
        verbose_name_plural = 'Блок футера'

    # fields

    def __str__(self):
        return 'Блок футера'


