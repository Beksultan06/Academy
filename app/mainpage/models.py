from django.db import models
from ckeditor.fields import RichTextField

class Settings(models.Model):
    phone_header = models.CharField(
        max_length=155,
        verbose_name='Номер телефона в Хедере'
    )
    date_header = models.CharField(
        max_length=155,
        verbose_name='Дата в Хедере'
    )
    date_header = models.CharField(
        max_length=155,
        verbose_name='Дата в Хедере',
        help_text='Раджаба Дата'
    )
    insta_url = models.URLField(
        verbose_name='Ссылка на Инстаграм'
    )
    face_book = models.URLField(
        verbose_name='Ссылка на Фейсбук'
    )
    email_footer = models.CharField(
        max_length=155,
        verbose_name='Почта на футоре'
    )
    location = models.CharField(
        max_length=355,
        verbose_name='Локация'
    )
    title_banner = models.CharField(
        max_length=155,
        verbose_name='Заголовка Баннера'
    )
    description_banner = RichTextField(
        verbose_name='Описание Баннера'
    )
    image_banner = models.ImageField(
        upload_to='settings',
        verbose_name='Фото Баннера'
    )
    title_news = models.CharField(
        max_length=155,
        verbose_name='Заголовка Новости'
    )
    title_scientific_degrees = models.CharField(
        max_length=155,
        verbose_name='Заголовка научные степени'
    )
    title_additional_professional_education = models.CharField(
        max_length=155,
        verbose_name='Заголовка дополнительная профессиональная образования'
    )
    title_courses = models.CharField(
        max_length=155,
        verbose_name='Заголовка Курсов'
    )
    title_we_suggest_you_watch_it = models.CharField(
        max_length=155,
        verbose_name='Заголовка Предлогаем к просмотру'
    )
    title_journal_of_the_islamic_academy = models.CharField(
        max_length=155,
        verbose_name='Заголовка журнал исламской академии'
    )
    title_journals_of_partner_universities = models.CharField(
        max_length=155,
        verbose_name='Заголовка журналы партнерских вузов'
    )
    title_gallery = models.CharField(
        max_length=155,
        verbose_name='Заголовка Галлерий'
    )
    obj_date = models.CharField(
        max_length=255,
        verbose_name='Дата Объекта Предлогаем к просмотру'
    )
    title_obj = models.CharField(
        max_length=155,
        verbose_name='Заголовка Объекта Предлогаем к просмотру'
    )
    description_obj = RichTextField(
        verbose_name='Описание Объекта Предлогаем к просмотру'
    )
    image_obj = models.ImageField(
        upload_to='settings/obj',
        verbose_name='Фото Объекта Предлогаем к просмотру'
    )

    def __str__(self):
        return self.title_banner


    class Meta:
        verbose_name = 'Настройки Главной Страницы'
        verbose_name_plural = 'Настройки Главной Страницы'


class NewsMain(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголловок')
    description = RichTextField(verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовки новостей'
        verbose_name_plural = 'Заголовки новостей'
    

class NewsCard(models.Model):
    page = models.ForeignKey(NewsMain, on_delete=models.CASCADE, related_name='cards')
    date = models.CharField(max_length=155,verbose_name='Заголловок')
    title = models.CharField(max_length=255)
    text = RichTextField(verbose_name='Заголловок')
    image = models.ImageField(upload_to='cards/', verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новостей'
        verbose_name_plural = 'новостей'

class Magazine(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголловок')
    description = RichTextField(verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовки Журналов'
        verbose_name_plural = 'Заголовки Журналов'

class MagazineCard(models.Model):
    page = models.ForeignKey(Magazine, on_delete=models.CASCADE, related_name='cards')
    date = models.CharField(max_length=155, verbose_name='Заголловок')
    title = models.CharField(max_length=255, verbose_name='Заголловок')
    text = RichTextField(verbose_name='Заголловок')
    image = models.ImageField(upload_to='missions/', verbose_name='Заголловок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Журналов'
        verbose_name_plural = 'Журналов'