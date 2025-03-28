from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
#О нас

class Name(models.Model):
    title = models.CharField(max_length=225,
    verbose_name = 'Об Академии')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'AboutAcademy name'
        verbose_name_plural = 'AboutAcademy name'


class AboutUs(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    title_phone_number = models.CharField(max_length=100,verbose_name='Заголовок номера телефона')
    phone_number = RichTextField(verbose_name='Номер телефона')
    title_adress = models.CharField(max_length=100,verbose_name='Заголовок адреса')
    adress = RichTextField(verbose_name='Адрес')
    title_operating_mode = models.CharField(max_length=100,verbose_name='Заголовок режима работы')
    operating_mode = RichTextField(verbose_name='Режим работы')
    link_map = models.URLField(verbose_name='Ссылка на карту')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class DevStrategy(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Стратегия развития'
        verbose_name_plural = 'Стратегии развития'


class Mission(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Миссия'
        verbose_name_plural = 'Миссии'

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')

    class Meta:
        ordering = ['id'] 
        verbose_name = "Документ"
        verbose_name_plural = "Документы"  
    


class Achievements(models.Model):
    title = models.TextField(
        verbose_name='Заголовок'
        )
    image = models.ImageField(
        upload_to='image/'
        )
    description = RichTextField(
        verbose_name='Описание'
        )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

class AchievementsObject(models.Model):
    achievements = models.ForeignKey(Achievements, on_delete=models.CASCADE,verbose_name='Достижение')
    image = models.ImageField(upload_to='dosti', verbose_name='Фото достижений')

    def __str__(self):
        return str(self.achievements.title)  

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Изображение'

class History(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

class HistoryObject(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE,verbose_name='Изображение истории слайдер')
    image = models.ImageField(upload_to='object_history_photos/',verbose_name='Фото объекта истории слайдер')

    def __str__(self):
        return str(self.history)  

    class Meta:
        verbose_name = 'Изображение истории слайдер'
        verbose_name_plural = 'Изображения истории слайдер'

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