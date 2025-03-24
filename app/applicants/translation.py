from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Name)
class NameTranslationOptions(TranslationOptions):
    fields = ('title',)
    
@register(Academic)
class AcademicTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Admissions_Committee)
class Admissions_CommitteeTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)