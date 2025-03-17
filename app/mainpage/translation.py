from modeltranslation.translator import register, TranslationOptions, translator
from .models import Banner, News, Degree, Recommendation, AcademyJournal, PartnerJournal, GalleryImage

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ("title", "description")

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "content", "detail_description")

@register(Degree)
class DegreeTranslationOptions(TranslationOptions):
    fields = ("name", "description")

@register(Recommendation)
class RecommendationTranslationOptions(TranslationOptions):
    fields = ("title", "description","detail_description")

@register(AcademyJournal)
class AcademyJournalTranslationOptions(TranslationOptions):
    fields = ("title", "description","detail_description")

@register(PartnerJournal)
class PartnerJournalTranslationOptions(TranslationOptions):
    fields = ("title", "description","detail_description")

@register(GalleryImage)
class GalleryImageTranslationOptions(TranslationOptions):
    fields = ("description",)
