from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    page_key = models.CharField(
        max_length=100,
        verbose_name="Ключ страницы (пример: about, history, mission)",
        help_text="Используется для группировки и отображения",
        blank=True,
        null=True
    )
    title_main = models.CharField(max_length=200, verbose_name="Главная Заголовка", blank=True, null=True)
    title2 = models.CharField(max_length=155, verbose_name='Под Заголовка', blank=True, null=True)
    title_page = models.CharField(max_length=155, verbose_name='Заголовка Страницы', blank=True, null=True)
    description = RichTextField(verbose_name='Данные о Страницы', blank=True, null=True)
    addresses = RichTextField(verbose_name='Адресы, телефон номер, режим работы', blank=True, null=True)
    links_carta = models.URLField(verbose_name='Ссылка на карту', blank=True, null=True)

    title_pdf = models.CharField(max_length=155, verbose_name='Заголовка Файла', blank=True, null=True)
    url_pdf = models.URLField(verbose_name='Ссылка на Файл', blank=True, null=True)
    dowl_url = models.FileField(verbose_name='PDF-Файл', blank=True, null=True)

    def __str__(self):
        return self.title_page or "About Page"

    class Meta:
        verbose_name = 'Об Академий'
        verbose_name_plural = 'Об Академий'

class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about-academy/', verbose_name='Фото')

    def __str__(self):
        return f"Изображение для {self.about.title_page}"

    class Meta:
        verbose_name = 'Изображение для страницая'
        verbose_name_plural = 'Изображение для страницая'