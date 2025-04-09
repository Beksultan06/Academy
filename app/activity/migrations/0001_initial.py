# Generated by Django 4.2.7 on 2025-04-05 06:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('title_ky', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('title_tr', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('title_ar', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Заголовка')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('description_tr', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ar', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('date', models.CharField(max_length=155, verbose_name='Дата')),
                ('date_ru', models.CharField(max_length=155, null=True, verbose_name='Дата')),
                ('date_ky', models.CharField(max_length=155, null=True, verbose_name='Дата')),
                ('date_tr', models.CharField(max_length=155, null=True, verbose_name='Дата')),
                ('date_ar', models.CharField(max_length=155, null=True, verbose_name='Дата')),
                ('date_en', models.CharField(max_length=155, null=True, verbose_name='Дата')),
                ('title_obj', models.CharField(max_length=155, verbose_name='Заголовка Объекта')),
                ('title_obj_ru', models.CharField(max_length=155, null=True, verbose_name='Заголовка Объекта')),
                ('title_obj_ky', models.CharField(max_length=155, null=True, verbose_name='Заголовка Объекта')),
                ('title_obj_tr', models.CharField(max_length=155, null=True, verbose_name='Заголовка Объекта')),
                ('title_obj_ar', models.CharField(max_length=155, null=True, verbose_name='Заголовка Объекта')),
                ('title_obj_en', models.CharField(max_length=155, null=True, verbose_name='Заголовка Объекта')),
                ('description_obj', ckeditor.fields.RichTextField(verbose_name='Описание Объекта')),
                ('description_obj_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание Объекта')),
                ('description_obj_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание Объекта')),
                ('description_obj_tr', ckeditor.fields.RichTextField(null=True, verbose_name='Описание Объекта')),
                ('description_obj_ar', ckeditor.fields.RichTextField(null=True, verbose_name='Описание Объекта')),
                ('description_obj_en', ckeditor.fields.RichTextField(null=True, verbose_name='Описание Объекта')),
                ('image', models.ImageField(upload_to='activity', verbose_name='Фото')),
                ('place', models.CharField(max_length=155, verbose_name='Место')),
                ('place_ru', models.CharField(max_length=155, null=True, verbose_name='Место')),
                ('place_ky', models.CharField(max_length=155, null=True, verbose_name='Место')),
                ('place_tr', models.CharField(max_length=155, null=True, verbose_name='Место')),
                ('place_ar', models.CharField(max_length=155, null=True, verbose_name='Место')),
                ('place_en', models.CharField(max_length=155, null=True, verbose_name='Место')),
                ('link', models.CharField(max_length=155, verbose_name='Категория')),
                ('link_ru', models.CharField(max_length=155, null=True, verbose_name='Категория')),
                ('link_ky', models.CharField(max_length=155, null=True, verbose_name='Категория')),
                ('link_tr', models.CharField(max_length=155, null=True, verbose_name='Категория')),
                ('link_ar', models.CharField(max_length=155, null=True, verbose_name='Категория')),
                ('link_en', models.CharField(max_length=155, null=True, verbose_name='Категория')),
            ],
        ),
    ]
