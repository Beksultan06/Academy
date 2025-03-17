from modeltranslation.translator import TranslationOptions, translator, register
from app.education.models import *

@register(WelcomePage)
class WelcomePageOptions(TranslationOptions):
    fields = ('title_welcome', 'information_title_welcome', 'information')

@register(EducationMiddle)
class EducationMiddleOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education')

@register(EducationMiddleObjects)
class EducationMiddleObjectsTranslationOptions(TranslationOptions):
    fields = ('title_object', 'title2_object')
    
@register(WelcomePageObjects)
class WelcomePageObjectsTranslationOptions(TranslationOptions):
    fields = ('title2_object', )

#Ape - Дополнительное Профессиональная Образование
@register(Ape)
class ApeTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(Courses)
class CoursesTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(Library)
class LibraryTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(EducationPro)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education')


@register(EducationSenior)
class EducationSeniorTranslationOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education')


@register(EducationDoctora)
class EducationDoctoraTranslationOptions(TranslationOptions):
    fields = ('title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education')

    
