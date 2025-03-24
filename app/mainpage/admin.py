from django.contrib import admin
from app.mainpage.models import Banner, News, Degree, Recommendation, AcademyJournal, PartnerJournal, GalleryImage
from modeltranslation.admin import TranslationAdmin
from .translation import *

class BannerAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky')}),
        ("Английская версия", {'fields': ('title_en', 'description_en')}),
        ("Туркская версия", {'fields': ('title_tr', 'description_tr')}),
        ("Арабская версия", {'fields': ('title_ar', 'description_ar')}),
        ("Изображение", {'fields': ('image',)}),
    )
    
class NewsAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'content_ru','detail_description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'content_ky','detail_description_ky')}),
        ("Английская версия", {'fields': ('title_en', 'content_en','detail_description_en')}),
        ("Туркская версия", {'fields': ('title_tr', 'content_tr', 'detail_description_tr')}),
        ("Арабская версия", {'fields': ('title_ar', 'content_ar', 'detail_description_ar')}),
        ("Изображение", {'fields': ('image',)}),
        ("Дата создания", {'fields': ('created_at',)}),
    )

class DegreeAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('name_ru', 'description_ru')}),
        ("Кыргызская версия", {'fields': ('name_ky', 'description_ky')}),
        ("Английская версия", {'fields': ('name_en', 'description_en')}),
        ("Туркская версия", {'fields': ('name_tr', 'description_tr')}),
        ("Арабская версия", {'fields': ('name_ar', 'description_ar')}),
    )

class RecommendationAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru','detail_description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky','detail_description_ky')}),
        ("Английская версия", {'fields': ('title_en', 'description_en', 'detail_description_en')}),
        ("Туркская версия", {'fields': ('title_tr', 'description_tr','detail_description_tr')}),
        ("Арабская версия", {'fields': ('title_ar', 'description_ar','detail_description_ar')}),
        ("Изображение", {'fields': ('image',)}),
        ("Дата создания", {'fields': ('created_at',)}),
    )

class AcademyJournalAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru','detail_description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky','detail_description_ky')}),
        ("Английская версия", {'fields': ('title_en', 'description_en','detail_description_en')}),
        ("Туркская версия", {'fields': ('title_tr', 'description_tr','detail_description_tr')}),
        ("Арабская версия", {'fields': ('title_ar', 'description_ar','detail_description_ar')}),
        ("Изображение", {'fields': ('image',)}),
        ("Дата создания", {'fields': ('created_at',)}),
    )

class PartnerJournalAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru','detail_description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky','detail_description_ky')}),
        ("Английская версия", {'fields': ('title_en', 'description_en','detail_description_en')}),
        ("Туркская версия", {'fields': ('title_tr', 'description_tr','detail_description_tr')}),
        ("Арабская версия", {'fields': ('title_ar', 'description_ar','detail_description_ar')}),
        ("Изображение", {'fields': ('image',)}),
        ("Дата создания", {'fields': ('created_at',)}),
    )



class GalleryImageAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('description_ru',)}),
        ("Кыргызская версия", {'fields': ('description_ky',)}),
        ("Английская версия", {'fields': ('description_en',)}),
        ("Туркская версия", {'fields': ('description_tr',)}),
        ("Арабская версия", {'fields': ('description_ar',)}),
        ("Изображение", {'fields': ('image',)}),
    )

admin.site.register(Banner, BannerAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(AcademyJournal, AcademyJournalAdmin)
admin.site.register(PartnerJournal, PartnerJournalAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
