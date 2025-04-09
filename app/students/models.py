from django.db import models
from ckeditor.fields import RichTextField


class ScientificJournal(models.Model):
    title = models.CharField(max_length=225, verbose_name='Тип информации', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class ScientificJournalObject(models.Model): 
    student = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE, verbose_name='Студент')
    image = models.ImageField(verbose_name='Image', blank=True, null=True, upload_to='students')


    class Meta:
        verbose_name = 'Обекты Студента'
        verbose_name_plural = 'Объекты Студентов'


class ScientificJournalWork(models.Model):
    student = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE, related_name='works', verbose_name='Студент')
    name = models.CharField(max_length=255, verbose_name='Название работы')
    description = models.TextField(verbose_name='Описание работы')
    img = models.ImageField(upload_to='work/', verbose_name='Изображение работы')

    class Meta:
        verbose_name = 'Работа студента'
        verbose_name_plural = 'Работы студентов'
