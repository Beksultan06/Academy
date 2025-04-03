from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(ScientificJournal)
class ScientificJournalsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'students_full_name',)
