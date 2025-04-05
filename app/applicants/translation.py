from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Academic)
class AcademicTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
