from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Name)
class NameTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ScientificJournalsObject)
class ScientificJournalsObjectTranslationOptions(TranslationOptions):
    fields = ('title2_object',)

@register(AcademicCouncil)
class AcademicCouncilTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(ScientificJournals)
class ScientificJournalsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(CenterEducation)
class CenterEducationTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
