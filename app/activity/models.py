from django.db import models
from ckeditor.fields import RichTextField

class Name(models.Model):
    title = models.CharField(max_length=225,
    verbose_name = 'Деятельность')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Activity name'
        verbose_name_plural = 'Activity name'

class Progress(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
        )
    description = RichTextField(
        max_length=255,
        verbose_name="Описание"
        )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        
class AllProgress(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
        )
    date = models.CharField(
        max_length=255,
        verbose_name="Дата"
    )
    awarded = models.CharField(
        max_length=255,
        verbose_name="Присуждается"
    )
    achieve = RichTextField(  
        verbose_name="Достижение"
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Место'
    )
    image = models.ImageField(
        verbose_name="Фото Достижения",
        upload_to='Progress/'
    )

    class Meta:
        verbose_name = "Все Достижения"
        verbose_name_plural = "Все Достижения" 
        
class Educational(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
        )
    date = models.CharField(
        max_length=255,
        verbose_name="Дата"
    )
    awarded = models.CharField(
        max_length=255,
        verbose_name="Присуждается"
    )
    achieve = RichTextField(  
        verbose_name="Достижение"
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Место'
    )
    image = models.ImageField(
        verbose_name="Фото Достижения",
        upload_to='Progress/'
    )

    class Meta:
        verbose_name = "Воспитание"
        verbose_name_plural = "Воспитание" 

