from django.db import models
from ckeditor.fields import RichTextField

class Activity(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = RichTextField(
        verbose_name = 'Описание',
        blank=True, null=True
    )

    date = models.CharField(
        max_length = 155,
        verbose_name = 'Дата'
    )
    title_obj = models.CharField(
        max_length=155,
        verbose_name='Заголовка Объекта'
    )
    description_obj = RichTextField(
        verbose_name='Описание Объекта'
    )
    image = models.ImageField(
        upload_to='activity',
        verbose_name='Фото'
    )
    place = models.CharField(
        max_length = 155,
        verbose_name = 'Место'
    )
    link = models.CharField(max_length=155, verbose_name='Категория')

    def __str__(self):
        return  self.title

    class Mate:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельности'
