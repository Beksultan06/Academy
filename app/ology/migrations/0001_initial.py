# Generated by Django 4.2.7 on 2025-04-05 06:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Общество')),
                ('title_ru', models.CharField(max_length=225, null=True, verbose_name='Общество')),
                ('title_ky', models.CharField(max_length=225, null=True, verbose_name='Общество')),
                ('title_tr', models.CharField(max_length=225, null=True, verbose_name='Общество')),
                ('title_ar', models.CharField(max_length=225, null=True, verbose_name='Общество')),
                ('title_en', models.CharField(max_length=225, null=True, verbose_name='Общество')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_tr', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_ar', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('number', models.CharField(max_length=225, verbose_name='Номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('link', models.URLField(verbose_name='Сыллка')),
            ],
            options={
                'verbose_name': 'Общество',
                'verbose_name_plural': 'Общества',
            },
        ),
    ]
