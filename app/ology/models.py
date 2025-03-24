from django.db import models
from ckeditor.fields import RichTextField


class Name(models.Model):
    title = models.CharField(max_length=225,
    verbose_name = 'Наука')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ology name'
        verbose_name_plural = 'Ology name'

class AcademicCouncil(models.Model):
    title = models.CharField(max_length=225, verbose_name='Учёный совет')
    description = RichTextField(verbose_name='Описание')
    number = models.CharField(verbose_name='Номер', max_length=225)
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
        
    
class ScientificJournalsObject(models.Model): 
    journal = models.ForeignKey(ScientificJournals, on_delete=models.CASCADE, verbose_name='Издание научных журналов')
    
    
    title2_object = models.CharField(
        max_length=255,
        verbose_name="Под заголовок обьекта"
    )

    def __str__(self):
        return self.title2_object

    class Meta:
        verbose_name = 'Объекты изданий научных журналов'
        verbose_name_plural = 'Объекты изданий научных журналов'


class CenterEducation(models.Model):
    title = models.CharField(max_length=225, verbose_name='Центр образования')
    description = RichTextField(verbose_name='Описание')
    number = models.CharField(verbose_name='Номер', max_length=225)
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Центр образования'
        verbose_name_plural = 'Центры образования'
    