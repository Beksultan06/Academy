from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Name(models.Model):
    title = models.CharField(max_length=225,
    verbose_name = 'Абитуриентам')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Applicants name'
        verbose_name_plural = 'Applicants name'


class Academic(models.Model):
    title = models.CharField(max_length=225, verbose_name='Поступить в академию')
    description = RichTextField(verbose_name='Описание')
    number = models.CharField(max_length=255, verbose_name='Номер')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абитуриентам'
        verbose_name_plural = 'Абитуриентам'

class Admissions_Committee(models.Model):
    title = models.CharField(max_length=225, verbose_name='Поступить в академию')
    description = RichTextField(verbose_name='Описание')
    number = models.CharField(max_length=255, verbose_name='Номер')
    email = models.EmailField(verbose_name='Электронная почта')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'комитет абитуриентов'
        verbose_name_plural = 'комитеты абитуриентов'