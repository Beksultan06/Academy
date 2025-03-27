from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Name(models.Model):
    title = models.CharField(max_length=225,
    verbose_name = 'Студенты')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Students name'
        verbose_name_plural = 'Students name'

class Parliament(models.Model):
    students_full_name = RichTextField(
        max_length=255,
        verbose_name="ФИО студента" 
    )
    description = RichTextField(
        verbose_name="Описание студента"
    )
    images = models.ImageField(
        upload_to="image/",
        verbose_name="Фотография студента"
    )

    def __str__(self):
        return self.students_full_name
    
    class Meta:
        verbose_name = 'Студенчекий Парламент'
        verbose_name_plural = 'Студенчекий Парламент'

class Active_Students(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО студента"
    )
    
    description = RichTextField(
        verbose_name="Первый обзац описания студента"
    )

    descriptions = RichTextField(verbose_name="Второй обзац описания студента")

    images = models.ImageField(
        upload_to="image/",
        verbose_name="Фотография студента",
        blank=True, null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Активные Студенты'
        verbose_name_plural = 'Активные Студенты'

class StudentWork(models.Model):
    student = models.ForeignKey(
        Active_Students, 
        on_delete=models.CASCADE, 
        related_name="work"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название проекта"
    )
    description = models.TextField(
        verbose_name="Описание проекта"
    )
    img = models.ImageField(
        upload_to="image/work/",
        verbose_name="Изображение проекта",
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работы студентов'
        verbose_name_plural = 'Работы студентов'
        

class Active_StudentsAbout(models.Model):
    title = models.CharField(max_length=100,verbose_name="Заголовок информации студента")
    description = RichTextField(verbose_name="Описание информации студента")
    images = models.ImageField(upload_to="image/", verbose_name="Фотография", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Дополнительная информация о активных студентах'
        verbose_name_plural = 'Дополнительные информации о активных студентах'


class Hostel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = RichTextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Студенческое общежитие"
        verbose_name_plural = "Студенческое общежитие"

class HostelObject(models.Model):
    hostel = models.ForeignKey(Hostel, related_name='images', on_delete=models.CASCADE, verbose_name="Общежитие")
    images = models.ImageField(upload_to='hostel_photos/', blank=True, null=True, verbose_name="Фотографии общежития")

    def __str__(self):
        return self.hostel.title
    
    class Meta:
        verbose_name = 'Изображение общежития слайдер'
        verbose_name_plural = 'Изображения общежития слайдер'

        
class Portal(models.Model):
    title = RichTextField(verbose_name="Заголовок страницы")
    description = RichTextField(verbose_name="Описание страницы")
    contacts = RichTextField(verbose_name="Контакты")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Портал"
        verbose_name_plural = "Портал"

class StudentsLife(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = RichTextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Студенческая жизнь"
        verbose_name_plural = "Студенческии жизни"

class StudentsLifeObject(models.Model):
    hostel = models.ForeignKey(StudentsLife, on_delete=models.CASCADE, verbose_name="Общежитие")
    images = models.ImageField(upload_to='hostel_photos/', blank=True, null=True, verbose_name="Фотографии жизни студентов")

    def __str__(self):
        return self.hostel.title
    
    class Meta:
        verbose_name = 'Изображение жизни студентов слайдер'
        verbose_name_plural = 'Изображения жизни студентов слайдер'

class ListPages(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Список страниц'
        verbose_name_plural = 'Список страниц'

class ListPagesObject(models.Model):
    list_pages = models.ForeignKey(ListPages, on_delete=models.CASCADE,verbose_name='Список страниц')
    two_title = models.CharField(max_length=100,verbose_name='Под заголовок')

    def __str__(self):
        return str(self.list_pages)
    
    class Meta:
        verbose_name = 'Под заголовок для списка страниц'
        verbose_name_plural = 'Под заголовки для списка страниц'
