# Generated by Django 4.1.7 on 2024-01-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0010_remove_contactsblock_inst_link_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FooterBlock',
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='instagram_link',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ссылка на Instagram'),
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='tg_link',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ссылка на Telegram'),
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='vk_link',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ссылка на VK'),
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='whatsapp_link',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ссылка на Whatsapp'),
        ),
    ]
