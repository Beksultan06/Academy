from django.db import models
from ckeditor.fields import RichTextField


class ScientificJournal(models.Model):
    title = models.CharField(max_length=225, verbose_name='Тип информации', blank=True, null=True)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    students_full_name = RichTextField(verbose_name='Полное имя студента', blank=True, null=True)
    number = models.CharField(max_length=225, verbose_name='Номер', blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    link = models.URLField(verbose_name='Ссылка', blank=True, null=True)
    

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