from modeltranslation.translator import TranslationOptions, translator, register
from app.education.models import *

@register(Name)
class NameTranslationOptions(TranslationOptions):
    fields = ('title',)
    
@register(WelcomePage)
class WelcomePageOptions(TranslationOptions):
    fields = ('title_welcome', 'information_title_welcome', 'information')

@register(EducationMiddle)
class EducationMiddleOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education','status_education', 'form_education', 'perioud_education')
    

@register(EducationMiddleObjects)
class EducationMiddleObjectsTranslationOptions(TranslationOptions):
    fields = ('title2_object', )
    
@register(WelcomePageObjects)
class WelcomePageObjectsTranslationOptions(TranslationOptions):
    fields = ('title2_object', )

# Ape - Дополнительное Профессиональное Образование
@register(Ape)
class ApeTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(ApeObjects)
class ApeObjectTranslationOption(TranslationOptions):
    fields = ('title_object',)

@register(Courses)
class CoursesTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(CoursesObjects)
class CoursesObjectTranslationOption(TranslationOptions):
    fields = ('title_object',)

@register(Library)
class LibraryTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(LibraryObjects)
class LibraryObjectTranslationOption(TranslationOptions):
    fields = ('title_object',)

@register(EducationPro)
class EducationProTranslationOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education')

@register(EducationSenior)
class EducationSeniorTranslationOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education')

@register(EducationDoctora)
class EducationDoctoraTranslationOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education')

@register(EducationDoctoraObjects)
class EducationDoctoraObjectTranslationOptions(TranslationOptions):
    fields = ('title_object',)
    
@register(EducationProObjects)
class EducationProObjectsTranslationOptions(TranslationOptions):
    fields = ('title2_object',)

@register(EducationSeniorObjects)
class EducationSeniorObjectsTranslationOptions(TranslationOptions):
    fields = ('title_object',)
