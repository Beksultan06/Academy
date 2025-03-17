from modeltranslation.translator import register, TranslationOptions
from .models import AcademicCouncil, ScientificJournals, CenterEducation

@register(AcademicCouncil)
class AcademicCouncilTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(ScientificJournals)
class ScientificJournalsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(CenterEducation)
class CenterEducationTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
