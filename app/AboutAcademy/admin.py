from django.contrib import admin
from app.AboutAcademy.models import *
from app.AboutAcademy.translation import *
from modeltranslation.admin import TranslationAdmin

class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra = 1

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    inlines = [AboutImageInline]

    list_display = ('id', 'page_key', 'title_page', 'title_main')
    search_fields = ('title_page', 'page_key')
    fieldsets = (
        ("Ключ", {
            'fields': ('page_key',)
        }),
        ("Русская версия", {
            'fields': ('title_main_ru', 'title2_ru', 'title_page_ru', 'description_ru', 'addresses_ru', 'title_pdf_ru', )
        }),
        ("Кыргызская версия", {
            'fields': ('title_main_ky', 'title2_ky', 'title_page_ky', 'description_ky', 'addresses_ky', 'title_pdf_ky')
        }),
        ("Английская версия", {
            'fields': ('title_main_en', 'title2_en', 'title_page_en', 'description_en', 'addresses_en', 'title_pdf_en')
        }),
        ("Туркская версия", {
            'fields': ('title_main_tr', 'title2_tr', 'title_page_tr', 'description_tr', 'addresses_tr', 'title_pdf_tr')
        }),
        ("Арабская версия", {
            'fields': ('title_main_ar', 'title2_ar', 'title_page_ar', 'description_ar', 'addresses_ar', 'title_pdf_ar')
        }),
        ("Global", {
            'fields': ('url_pdf', 'dowl_url', 'links_carta',)
        }),
    )
