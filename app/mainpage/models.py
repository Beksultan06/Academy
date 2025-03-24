from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Banner(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = RichTextField("Описание")
    image = models.ImageField("Изображение", upload_to='banners/')

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

class News(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = RichTextField("Содержание")
    image = models.ImageField("Изображение", upload_to='news/')
    created_at = models.CharField("Дата создания", max_length=255)
    detail_description = RichTextField("Детальный просмотр")


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Degree(models.Model):
    name = models.CharField("Название", max_length=255)
    description = RichTextField("Описание")

    class Meta:
        verbose_name = "Научная степень"
        verbose_name_plural = "Научные степени"

class Recommendation(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = RichTextField("Описание")
    image = models.ImageField("Изображение", upload_to='recommendations/')
    detail_description = RichTextField("Детальный просмотр")
    created_at = models.CharField("Дата создания", max_length=255)

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"

class AcademyJournal(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = RichTextField("Описание")
    image = models.ImageField("Изображение", upload_to='journals/')
    created_at = models.CharField("Дата создания", max_length=255)
    detail_description = RichTextField("Детальный просмотр")

    class Meta:
        verbose_name = "Журнал Исламской Академии"
        verbose_name_plural = "Журналы Исламской Академии"

class PartnerJournal(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = RichTextField("Описание")
    image = models.ImageField("Изображение", upload_to='partner_journals/')
    created_at = models.CharField("Дата создания", max_length=255)
    detail_description = RichTextField("Детальный просмотр")


    class Meta:
        verbose_name = "Журнал Партнерских ВУЗов"
        verbose_name_plural = "Журналы Партнерских ВУЗов"

class GalleryImage(models.Model):
    image = models.ImageField("Изображение", upload_to='gallery/')
    description = RichTextField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Галерея"
