from modeltranslation.translator import translator, TranslationOptions, register
from app.activity.models import Activity

@register(Activity)
class ActivityTranslationOptions(TranslationOptions):
    fields = ("title", 'description', 'date', 'title_obj', 'description_obj', 'place', 'link')