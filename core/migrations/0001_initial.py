# Generated by Django 4.1.7 on 2023-04-22 17:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', ckeditor.fields.RichTextField(verbose_name='Вопрос')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='Ответ')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'часто задаваемый вопрос',
                'verbose_name_plural': 'часто задаваемые вопросы',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ReviewText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', ckeditor.fields.RichTextField(verbose_name='Имя автора отзыва')),
                ('review_text', ckeditor.fields.RichTextField(verbose_name='Текст отзыва')),
                ('author_photo', models.ImageField(blank=True, upload_to='authors/', verbose_name='Фото автора отзыва')),
                ('review_link', models.CharField(blank=True, max_length=1000, verbose_name='Ссылка на отзыв')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'текcтовый отзыв',
                'verbose_name_plural': 'текcтовые отзывы',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ReviewVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=500, upload_to='projects/', verbose_name='Превью отзыва')),
                ('video_link', models.CharField(max_length=1000, verbose_name='Ссылка на видео отзыв')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'видео отзыв',
                'verbose_name_plural': 'видео отзывы',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField(verbose_name='Имя')),
                ('post', ckeditor.fields.RichTextField(verbose_name='Должность')),
                ('image', models.ImageField(max_length=500, upload_to='team/', verbose_name='Фото')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'персонал',
                'verbose_name_plural': 'персонал',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(verbose_name='Текст этапа')),
                ('image', models.ImageField(max_length=500, upload_to='stages/', verbose_name='Фото этапа')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'cтадия работ',
                'verbose_name_plural': 'стадии работ',
                'ordering': ['order'],
            },
        ),
    ]
