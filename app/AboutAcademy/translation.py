from modeltranslation.translator import register, TranslationOptions
from app.AboutAcademy.models import *

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ("page_key", 'title_main', 'title2', 'title_page', 'description', 'addresses', 'title_pdf')