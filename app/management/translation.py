from modeltranslation.translator import register, TranslationOptions
from .models import Leadership, LeadershipType

@register(LeadershipType)
class LeadershipTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Leadership)
class LeadershipTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'name',
        'description',
        'responsibilities',
        'contact',
    )
