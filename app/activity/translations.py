from modeltranslation.translator import translator, TranslationOptions, register
from app.activity.models import *

@register(Name)
class NameTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Progress)
class ProgressTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(AllProgress)
class AllProgressTranslationOptions(TranslationOptions):  
    fields = ('awarded', 'achieve', 'location', 'date')
    
@register(Educational)
class EducationalTranslationOptions(TranslationOptions):  
    fields = ('title', 'awarded', 'achieve', 'location', 'date')


