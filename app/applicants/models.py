from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Academic(models.Model):
    title = models.CharField(max_length=225, verbose_name='Поступить в академию', blank=True, null=True )
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    number = models.CharField(max_length=255, verbose_name='Номер', blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абитуриентам'
        verbose_name_plural = 'Абитуриентам'

