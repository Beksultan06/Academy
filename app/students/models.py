from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Parliament (models.Model):
    title = RichTextField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = RichTextField(
        verbose_name="Описание"
    )
    images = models.ImageField(
        upload_to="image/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Студенчекий Парламент'
        verbose_name_plural = 'Студенчекий Парламент'

class Active (models.Model):
    title =RichTextField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = RichTextField(
        verbose_name="Описание"
    )
    images = models.ImageField(
        upload_to="image/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Активные Студенты'
        verbose_name_plural = 'Активные Студенты'

class Hostel(models.Model):
    title = RichTextField(verbose_name="Заголовок страницы")
    description = RichTextField(verbose_name="Описание страницы")

    accommodation_title = RichTextField(verbose_name="Заголовок для условий проживания")
    accommodation_text = RichTextField(verbose_name="Описание условий проживания")

    spiritual_title = RichTextField(verbose_name="Заголовок для духовной атмосферы")
    spiritual_text = RichTextField(verbose_name="Описание духовной атмосферы")


    security_title = RichTextField(verbose_name="Заголовок для безопасности и порядка")
    security_text = RichTextField(verbose_name="Описание безопасности и порядка")

 
    student_life_title = RichTextField(verbose_name="Заголовок для студенческого быта")
    student_life_text = RichTextField(verbose_name="Описание студенческого быта")

    reviews_title = RichTextField(verbose_name="Заголовок для отзывов студентов")
    reviews_text = RichTextField(verbose_name="Описание отзывов студентов")

    images = models.ImageField(upload_to='hostel_photos/', blank=True, null=True, verbose_name="Фотографии общежития")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Студенческое общежитие"
        verbose_name_plural = "Студенческое общежитие"

class StudentLife(models.Model):
    title = RichTextField(verbose_name="Заголовок страницы")
    description = RichTextField(verbose_name="Описание страницы")

    education_title = RichTextField(verbose_name="Заголовок для образования и науки")
    education_text = RichTextField(verbose_name="Описание для образования и науки")

    spiritual_development_title = RichTextField(verbose_name="Заголовок для духовного развития")
    spiritual_development_text = RichTextField(verbose_name="Описание духовного развития")

    cultural_events_title = RichTextField(verbose_name="Заголовок для культурных и общественных мероприятий")
    cultural_events_text = RichTextField(verbose_name="Описание культурных и общественных мероприятий")


    sports_title = RichTextField(verbose_name="Заголовок для спорта и здорового образа жизни")
    sports_text = RichTextField(verbose_name="Описание спорта и здорового образа жизни")

    reviews_title = RichTextField(verbose_name="Заголовок для отзывов студентов")
    reviews_text = RichTextField(verbose_name="Описание отзывов студентов")

    images = models.ImageField(upload_to='student_life_photos/', blank=True, null=True, verbose_name="Фотографии студенческой жизни")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Студенческая жизнь в академии"
        verbose_name_plural = "Студенческая жизнь в академии"
