from django.contrib import admin
from .models import AcademicCouncil, ScientificJournals, CenterEducation
from . translation import *
from modeltranslation.admin import TranslationAdmin

class AcademicCouncilAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабская версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкая версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
        ('Global', {
            'fields': ['number', 'email'],
        }),
    )


class ScientificJournalsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабская версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкая версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
        ('Global', {
            'fields': ['image', 'link'],
        }),
    )


class CenterEducationAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабская версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкая версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
        ('Global', {
            'fields': ['number', 'email'],
        }),
    )

admin.site.register(AcademicCouncil, AcademicCouncilAdmin)
admin.site.register(ScientificJournals, ScientificJournalsAdmin)
admin.site.register(CenterEducation, CenterEducationAdmin)
