from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(ScientificJournal)
class ScientificJournalsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(ScientificJournalWork)
class ScientificJournalWorkTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
