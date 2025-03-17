from django.db import models
from ckeditor.fields import RichTextField

class AcademicCouncil(models.Model):
    title = models.CharField(max_length=225, verbose_name='Учёный совет')
    description = RichTextField(verbose_name='Описание')
    number = models.IntegerField(verbose_name='Номер')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учёный совет'
        verbose_name_plural = 'Учёные советы'


class ScientificJournals(models.Model):
    title = models.CharField(max_length=225, verbose_name='Издание научных журналов')
    description = RichTextField(verbose_name='Описание')
    image = models.ImageField(upload_to='scientific')
    link = models.URLField(verbose_name='Ссылка на журнал')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Издание научных журналов'
        verbose_name_plural = 'Издания научных журналов'


class CenterEducation(models.Model):
    title = models.CharField(max_length=225, verbose_name='Центр образования')
    description = RichTextField(verbose_name='Описание')
    number = models.IntegerField(verbose_name='Номер')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Центр образования'
        verbose_name_plural = 'Центры образования'
    