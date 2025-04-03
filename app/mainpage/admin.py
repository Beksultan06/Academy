from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from app.mainpage.models import Settings
from .translation import *

@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ('title_banner', 'phone_header', 'email_footer')
    search_fields = ('title_banner', 'phone_header', 'email_footer', 'location')

    fieldsets = (
        ("📞 Хедер", {
            'fields': ('phone_header', 'date_header')
        }),
        ("📍 Подвал и Соц. сети", {
            'fields': ('email_footer', 'location', 'insta_url', 'face_book')
        }),
        ("🎯 Баннер", {
            'fields': (
                'title_banner_ru', 'title_banner_ky', 'title_banner_en', 'title_banner_tr', 'title_banner_ar',
                'description_banner_ru', 'description_banner_ky', 'description_banner_en', 'description_banner_tr', 'description_banner_ar',
                'image_banner'
            )
        }),
        ("📰 Блоки разделов", {
            'fields': (
                'title_news_ru', 'title_news_ky', 'title_news_en', 'title_news_tr', 'title_news_ar',
                'title_scientific_degrees_ru', 'title_scientific_degrees_ky', 'title_scientific_degrees_en', 'title_scientific_degrees_tr', 'title_scientific_degrees_ar',
                'title_additional_professional_education_ru', 'title_additional_professional_education_ky', 'title_additional_professional_education_en', 'title_additional_professional_education_tr', 'title_additional_professional_education_ar',
                'title_courses_ru', 'title_courses_ky', 'title_courses_en', 'title_courses_tr', 'title_courses_ar',
                'title_we_suggest_you_watch_it_ru', 'title_we_suggest_you_watch_it_ky', 'title_we_suggest_you_watch_it_en', 'title_we_suggest_you_watch_it_tr', 'title_we_suggest_you_watch_it_ar',
                'title_journal_of_the_islamic_academy_ru', 'title_journal_of_the_islamic_academy_ky', 'title_journal_of_the_islamic_academy_en', 'title_journal_of_the_islamic_academy_tr', 'title_journal_of_the_islamic_academy_ar',
                'title_journals_of_partner_universities_ru', 'title_journals_of_partner_universities_ky', 'title_journals_of_partner_universities_en', 'title_journals_of_partner_universities_tr', 'title_journals_of_partner_universities_ar',
                'title_gallery_ru', 'title_gallery_ky', 'title_gallery_en', 'title_gallery_tr', 'title_gallery_ar'
            )
        }),
        ("📺 Предлагаем к просмотру (Объект)", {
            'fields': (
                'obj_date',
                'title_obj_ru', 'title_obj_ky', 'title_obj_en', 'title_obj_tr', 'title_obj_ar',
                'description_obj_ru', 'description_obj_ky', 'description_obj_en', 'description_obj_tr', 'description_obj_ar',
                'image_obj'
            )
        }),
    )
