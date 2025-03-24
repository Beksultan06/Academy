from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Name(models.Model):
    title = models.CharField(max_length=225,
    verbose_name = 'Руководсво')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Management name'
        verbose_name_plural = 'Management name'


class Rector(models.Model):
    name_rector = models.CharField(
        max_length=255,
        verbose_name="Имя ректора"
        )
    job_title_rector = models.CharField(
        max_length=255,
        verbose_name="Должность ректора"
        )
    education_rector = models.CharField(
        max_length=255,
        verbose_name="Образование ректора(Доктор Гумонитарных Наук)"
    )
    image_rector = models.ImageField(
        verbose_name="Фото ректора",
        upload_to='rector/'
    )
    
    def __str__(self):
        return self.name_rector
    
    class Meta:
        verbose_name = "Ректор"
        verbose_name_plural = "Ректоры"
        
class RectorObjectsTitle(models.Model):
    rector = models.ForeignKey(
        Rector,
        on_delete=models.CASCADE, 
        verbose_name="rector"
        )
    title2 = models.CharField(
        max_length=255,
        verbose_name="Под заголовок объекта",
        default="Под заголовок объекта"
    )
    
    def __str__(self):
        return str(self.rector)
    
    class Meta:
        verbose_name = "Объект ректора"
        verbose_name_plural = "Объекты ректора"
        
class ScientWorksRector(models.Model):
    description_works = models.CharField(
        max_length=255,
        verbose_name="Описание научного труда ректора"
    )
    date_works = models.CharField(
        max_length=255,
        verbose_name="Дата публикации научного труда"
    )
    major_works = RichTextField(
        verbose_name="Основные работы ректора"
    )
    link_pdf_works = models.URLField(
        verbose_name="Ссылка на PDF-версию научного труда"
    )
    contacs_works = models.CharField(
        max_length=255,
        verbose_name="Контакты для связи",
        default="Контакты для связи"
    )
    email_works = models.EmailField(
        verbose_name="Email для связи",
        default="Контакты для связи"
    )
    phone_number_works = models.CharField(
        max_length=255,
        verbose_name="Номер телефона для связи",
        default="+7 (XXX) XXX-XX-XX"
    )
    
    def __str__(self):
        return "Научные труды ректора"
    
    class Meta:
        verbose_name = "Научные труды ректора"
        verbose_name_plural = "Научные труды ректора"
        
class ScientWorksRectorObjects(models.Model):
    scientworks_rector = models.ForeignKey(
        ScientWorksRector,
        on_delete=models.CASCADE, 
        verbose_name="научные труды ректора"
        )
    title2_works = models.CharField(
        max_length=255,
        verbose_name="Под заголовок объекта",
        default="Под заголовок объекта"
    )
    
    def __str__(self):
        return str(self.scientworks_rector)
    
    class Meta:
        verbose_name = "Объекты научных трудов ректора"
        verbose_name_plural = "Объекты научных трудов ректора"
    
class HR_department(models.Model):
    name_department = models.CharField(
        max_length=255,
        verbose_name="Название отдела HR"
    )
    description_department = models.CharField(
        max_length=255,
        verbose_name="Описание отдела HR"
    ) 
    our_tasks_department = RichTextField(
        verbose_name="Наши задачи в отделе HR"
    )
    head_department = models.CharField(
        max_length=255,
        verbose_name="Руководитель отдела HR"
    )
    contacs_department = models.CharField(
        max_length=255,
        verbose_name="Контакты отдела HR",
        default="Контакты для связи"
    )
    email_department = models.EmailField(
        verbose_name="Email отдела HR",
        default="Контакты для связи"
    )
    phone_number_department = models.CharField(
        max_length=255,
        verbose_name="Номер телефона для связи",
        default="+7 (XXX) XXX-XX-XX"
    )
    def __str__(self):
        return self.name_department
    
    class Meta:
        verbose_name = "Отдел HR"
        verbose_name_plural = "Отделы HR"
        
class HR_departmentObjects(models.Model):
    hr_department = models.ForeignKey(
        HR_department,
        on_delete=models.CASCADE, 
        verbose_name="отдел HR"
        )
    title2_department = models.CharField(
        max_length=255,
        verbose_name="Под заголовок объекта",
        default="Объект для вакансии",
        null=True,
        blank=True
    )
    
    def __str__(self):
        return str(self.hr_department)
    
    class Meta:
        verbose_name = "Объекты вакансий отдела HR"
        verbose_name_plural = "Объекты вакансий отдела HR"
    
class Vacancies(models.Model):
    name_vacancy = models.CharField(
        max_length=255,
        verbose_name="Название вакансии"
    )
    responsibilities_vacancy = models.CharField(
        max_length=255,
        verbose_name="Обязанности вакансии"
    )
    date_vacancy = models.CharField(
        max_length=255,
        verbose_name="Дата публикации вакансии"
    )
    teacher_islamic_sciences_vacancy = RichTextField(
        verbose_name="Преподаватель исламских наук"
    )
    contacs_vacancy = models.CharField(
        max_length=255,
        verbose_name="Контакты отдела HR",
        default="Контакты для связи"
    )
    email_vacancy = models.EmailField(
        verbose_name="Email отдела HR",
        default="Контакты для связи"
    )
    phone_number_vacancy = models.CharField(
        max_length=255,
        verbose_name="Номер телефона для связи",
        default="+7 (XXX) XXX-XX-XX"
    )
    def __str__(self):
        return self.name_vacancy
    
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        
class VacanciesObjects(models.Model):
    vacancy = models.ForeignKey(
        Vacancies,
        on_delete=models.CASCADE, 
        verbose_name="вакансия"
        )
    title2_vacancy = models.CharField(
        max_length=255,
        verbose_name="Под заголовок объекта",
        default="Под заголовок объекта"
    )
    
    def __str__(self):
        return str(self.vacancy)
    
    class Meta:
        verbose_name = "Объекты вакансий"
        verbose_name_plural = "Объекты вакансий"