from modeltranslation.translator import translator, TranslationOptions, register
from app.activity.models import Progress, AllProgress, Educational

@register(Progress)
class ProgressTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(AllProgress)
class AllProgressTranslationOptions(TranslationOptions):  
    fields = ('awarded', 'achieve', 'location', 'date')
    
@register(Educational)
class EducationalTranslationOptions(TranslationOptions):  
    fields = ('title', 'awarded', 'achieve', 'location', 'date')


