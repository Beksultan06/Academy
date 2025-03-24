from django.db import models

# Create your models here.
class Photos(models.Model):
    photo = models.ImageField(upload_to='photos')
    date = models.CharField(max_length=155, verbose_name='Дата')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
