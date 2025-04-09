from django.db import models
from ckeditor.fields import RichTextField


class Ology(models.Model):
    title = models.CharField(max_length=225, verbose_name='Общество', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    number = models.CharField(verbose_name='Номер', max_length=225, blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    link = models.URLField(verbose_name='Сыллка', blank=True, null=True)
    image = models.ImageField(upload_to='ology', verbose_name='Фото', blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Общество'
        verbose_name_plural = 'Общества'
