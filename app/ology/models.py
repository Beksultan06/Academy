from django.db import models
from ckeditor.fields import RichTextField


class Ology(models.Model):
    title = models.CharField(max_length=225, verbose_name='Общество')
    description = RichTextField(verbose_name='Описание')
    number = models.CharField(verbose_name='Номер', max_length=225)
    email = models.EmailField(verbose_name='Электронная почта')
    link = models.URLField(verbose_name='Сыллка')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Общество'
        verbose_name_plural = 'Общества'
