from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Ology)
class OlogyTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
