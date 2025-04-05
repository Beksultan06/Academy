from django.db import models
from ckeditor.fields import RichTextField

class LeadershipType(models.Model):
    code = models.SlugField(max_length=50, unique=True, verbose_name="Код (напр. rector)")
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

class Leadership(models.Model):
    type = models.ForeignKey(LeadershipType, on_delete=models.CASCADE, related_name="items", verbose_name="Тип")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    description = RichTextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to="leadership/", blank=True, null=True)
    link = models.URLField(max_length=255, verbose_name="Ссылка на файл", blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name="Почта", blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name="Телефон", blank=True, null=True)
    contact = models.CharField(max_length=255, verbose_name="Контакт", blank=True, null=True)
    responsibilities = RichTextField(verbose_name="Обязанности, Требования, Условия", blank=True, null=True)
    date_publication = models.CharField(max_length=255, verbose_name="Дата публикации", blank=True, null=True)

    def __str__(self):
        return f"{self.type.name}: {self.title}"

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Руководство / Отделы / Вакансии"
