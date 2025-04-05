from modeltranslation.translator import TranslationOptions, register
from .models import *


@register(AllEducation)
class AllEducationTranslationOptions(TranslationOptions):
    fields = (
        'title', 'description', 'link'
    )

@register(AllEducationObject)
class AllEducationObjectTranslationOptions(TranslationOptions):
    fields = (
        'name_speciality_education', 'status_education', 'form_education', 'perioud_education'
    )