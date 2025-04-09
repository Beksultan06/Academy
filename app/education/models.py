from django.db import models
from ckeditor.fields import RichTextField

class AllEducation(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок объекта", blank=True, null=True)
    description = RichTextField(verbose_name="Описание", blank=True, null=True)
    link = models.CharField(max_length=255, verbose_name="Категория", blank=True, null=True)

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"

    def __str__(self):
        return self.title

class AllEducationObject(models.Model):
    educations = models.ForeignKey(AllEducation, on_delete=models.CASCADE, verbose_name='Объекты Образования')
    name_speciality_education = models.CharField(max_length=255, verbose_name="Название специальности", blank=True, null=True)
    status_education = models.CharField(max_length=255, verbose_name="Статус обучения", blank=True, null=True)
    form_education = models.CharField(max_length=255, verbose_name="Форма обучения", blank=True, null=True)
    perioud_education = models.CharField(max_length=255, verbose_name="Период обучения", blank=True, null=True)
