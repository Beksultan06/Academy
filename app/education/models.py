from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Name(models.Model):
    title = models.CharField(max_length=225,
    verbose_name = 'Образавание')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Education name'
        verbose_name_plural = 'Education name'


class WelcomePage(models.Model):
    title_welcome = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
        )
    information_title_welcome = models.CharField(
        max_length=255,
        verbose_name="Заголовок информации"
        )
    information = RichTextField(
        verbose_name="Информация"
    )
    
    def __str__(self):
        return self.title_welcome
    
    class Meta:
        verbose_name = "Страница приветствия"
        verbose_name_plural = "Страницы приветствия"
        
class WelcomePageObjects(models.Model):
    welcome_page = models.ForeignKey(
        WelcomePage,
        on_delete=models.CASCADE, 
        verbose_name="страница приветствия"
        )
    title2_object = models.CharField(
        max_length=255,
        verbose_name="Под заголовок обьекта"
    )
    
    def __str__(self):
        return self.title2_object
    
    class Meta:
        verbose_name = "Объекты страницы приветствия"
        verbose_name_plural = "Объекты страницы приветствия"
    
from django.db import models
from ckeditor.fields import RichTextField

class EducationMiddle(models.Model):
    # начало страницы
    title_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок образования среднего уровня"
    )
    description_education = RichTextField(
        verbose_name="Описание образования среднего уровня"
    )
    title_facult_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок факультета образования среднего уровня"
    )
    description_facult_education = RichTextField(
        verbose_name="Описание факультета образования среднего уровня"
    )

    # вводимые поля таблицы
    name_speciality_education = models.CharField(
        max_length=255,
        verbose_name="Название специальности"
    )
    status_education = models.CharField(
        max_length=255,
        verbose_name="Статус специальности"
    )
    form_education = models.CharField(
        max_length=255,
        verbose_name="Форма обучения"
    )
    perioud_education = models.CharField(
        max_length=255,
        verbose_name="Период обучения"
    )

    def __str__(self):
        return f"{self.title_education} - {self.name_speciality_education}"

    class Meta:
        verbose_name = "Образование среднего уровня"
        verbose_name_plural = "Образование среднего уровня"

class EducationMiddleObjects(models.Model):
    education_middle = models.ForeignKey(
        EducationMiddle,
        on_delete=models.CASCADE, 
        verbose_name="образование среднего уровня"
        )
    title2_object = models.CharField(
        max_length=255,
        verbose_name="Под заголовок"
    )
    def __str__(self):
        return self.title2_object
    
    class Meta:
        verbose_name = "Объекты образования среднего уровня"
        verbose_name_plural = "Объекты образования среднего уровня"
# Create your models here.

#Ape - Дополнительное Профессиональная Образование
class Ape(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Дополнительное профессиональное образование'
        verbose_name_plural = 'Дополнительное профессиональное образование'

class Courses(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок курса')
    description = RichTextField(verbose_name='Описание курса')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Library(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок библиотеки')
    description = RichTextField(verbose_name='Описание библиотеки')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'
    


class EducationPro(models.Model):
    title_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок образования вышего уровня"
    )
    description_education = RichTextField(
        verbose_name="Описание образования вышего уровня"
    )
    title_facult_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок факультета образования вышего уровня"
    )
    description_facult_education = RichTextField(
        verbose_name="Описание факультета образования вышего уровня"
    )
    name_speciality_education = models.CharField(
        max_length=255,
        verbose_name="Название специальности"
    )
    status_education = models.CharField(
        max_length=255,
        verbose_name="Статус специальности"
    )
    form_education = models.CharField(
        max_length=255,
        verbose_name="Форма обучения"
    )
    perioud_education = models.CharField(
        max_length=255,
        verbose_name="Период обучения"
    )

    def __str__(self):
        return self.title_education

    class Meta:
        verbose_name = "Образование высокого уровня"
        verbose_name_plural = "Образование высокого уровня"


class EducationProObjects(models.Model):
    education_pro = models.ForeignKey(
        EducationPro,
        on_delete=models.CASCADE,
        verbose_name="Образование высокого уровня"
    )
    title2_object = models.CharField(
        max_length=255,
        verbose_name="Заголовок объекта"
    )

    def __str__(self):
        return self.title2_object

    class Meta:
        verbose_name = "Объекты образования высокого уровня"
        verbose_name_plural = "Объекты образования высокого уровня"


class EducationSenior(models.Model):
    title_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок Магистратуры"
    )
    description_education = RichTextField(
        verbose_name="Описание Магистратуры"
    )
    title_facult_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок факультета Магистратуры"
    )
    description_facult_education = RichTextField(
        verbose_name="Описание факультета Магистратуры"
    )
    name_speciality_education = models.CharField(
        max_length=255,
        verbose_name="Название специальности"
    )
    status_education = models.CharField(
        max_length=255,
        verbose_name="Статус специальности"
    )
    form_education = models.CharField(
        max_length=255,
        verbose_name="Форма обучения"
    )
    perioud_education = models.CharField(
        max_length=255,
        verbose_name="Период обучения"
    )

    def __str__(self):
        return self.title_education

    class Meta:
        verbose_name = "Магистратура"
        verbose_name_plural = "Магистратуры"


class EducationSeniorObjects(models.Model):
    education_senior = models.ForeignKey(
        EducationSenior,
        on_delete=models.CASCADE,
        verbose_name="Магистратура"
    )
    title_object = models.CharField(
        max_length=255,
        verbose_name="Заголовок объекта"
    )

    def __str__(self):
        return self.title_object

    class Meta:
        verbose_name = "Объекты Магистратуры"
        verbose_name_plural = "Объекты Магистратуры"


class EducationDoctora(models.Model):
    title_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок Докторунтуры"
    )
    description_education = RichTextField(
        verbose_name="Описание Докторунтуры"
    )
    title_facult_education = models.CharField(
        max_length=255,
        verbose_name="Заголовок факультета Докторунтуры"
    )
    description_facult_education = RichTextField(
        verbose_name="Описание факультета Докторунтуры"
    )
    name_speciality_education = models.CharField(
        max_length=255,
        verbose_name="Название специальности"
    )
    status_education = models.CharField(
        max_length=255,
        verbose_name="Статус специальности"
    )
    form_education = models.CharField(
        max_length=255,
        verbose_name="Форма обучения"
    )
    perioud_education = models.CharField(
        max_length=255,
        verbose_name="Период обучения"
    )

    def __str__(self):
        return self.title_education

    class Meta:
        verbose_name = "Докторунтура"
        verbose_name_plural = "Докторунтуры"


class EducationDoctoraObjects(models.Model):
    education_doctora = models.ForeignKey(
        EducationDoctora,
        on_delete=models.CASCADE,
        verbose_name="Докторунтура"
    )
    title_object = models.CharField(
        max_length=255,
        verbose_name="Заголовок объекта"
    )

    def __str__(self):
        return self.title_object

    class Meta:
        verbose_name = "Объекты Докторунтуры"
        verbose_name_plural = "Объекты Докторунтуры"

class ApeObjects(models.Model):
    education_ape = models.ForeignKey(
        "Ape",
        on_delete=models.CASCADE,
        verbose_name="Образование дополнительного уровня"
    )
    title_object = models.CharField(
        max_length=255,
        verbose_name="Заголовок объекта"
    )

    def __str__(self):
        return self.title_object

    class Meta:
        verbose_name = "Объект Дополнительное Профессиональная Образование"
        verbose_name_plural = "Объекты Дополнительное Профессиональная Образование"
        
class CoursesObjects(models.Model):
    education_courses = models.ForeignKey(
        "Courses",
        on_delete=models.CASCADE,
        verbose_name="Образование дополнительного уровня"
    )
    title_object = models.CharField(
        max_length=255,
        verbose_name="Заголовок объекта"
    )

    def __str__(self):
        return self.title_object

    class Meta:
        verbose_name = "Объект Дополнительное Профессиональная Образование"
        verbose_name_plural = "Объекты Дополнительное Профессиональная Образование"
        
class LibraryObjects(models.Model):
    education_library = models.ForeignKey(
        "Library",
        on_delete=models.CASCADE,
        verbose_name="Образование дополнительного уровня"
    )
    title_object = models.CharField(
        max_length=255,
        verbose_name="Заголовок объекта"
    )

    def __str__(self):
        return self.title_object

    class Meta:
        verbose_name = "Объект Дополнительное Профессиональная Образование"
        verbose_name_plural = "Объекты Дополнительное Профессиональная Образование"
