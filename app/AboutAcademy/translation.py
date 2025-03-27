from modeltranslation.translator import register, TranslationOptions
from app.AboutAcademy.models import *

@register(Name)
class NameTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(AboutUs)
class AboutUsTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'title_phone_number', 'phone_number', 'title_adress', 'adress', 'title_operating_mode', 'operating_mode', 'link_map')

@register(DevStrategy)
class DevStrategyTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(Mission)
class MissionTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(Document)
class DocumentTranslationOption(TranslationOptions):
    fields = ('title', 'title_2',)


@register(Achievements)
class AchievementsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


@register(History)
class HistoryTranslationOption(TranslationOptions):
    fields = ('title','description')

@register(ListPages)
class ListPagesTranslationOption(TranslationOptions):
    fields = ('title',)

@register(ListPagesObject)
class ListPagesObjectTranslationOption(TranslationOptions):
    fields = ('two_title',)
