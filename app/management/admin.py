from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import LeadershipType, Leadership
from .translation import *

@admin.register(LeadershipType)
class LeadershipTypeAdmin(TranslationAdmin):
    list_display = ('name', 'code')
    prepopulated_fields = {'code': ('name',)}

@admin.register(Leadership)
class LeadershipAdmin(TranslationAdmin):
    list_display = ('title', 'type', 'name', 'email', 'phone', 'date_publication')
    list_filter = ('type',)
    search_fields = ('title', 'name', 'email', 'phone', 'contact')
    ordering = ('-date_publication',)

    fieldsets = (
        ("Основная информация", {
            'fields': ('type', 'title', 'name', 'description', 'image')
        }),
        ("Контактные данные и файл", {
            'fields': ('link', 'email', 'phone', 'contact', 'date_publication')
        }),
        ("Обязанности, Требования, Условия", {
            'fields': ('responsibilities',)
        }),
    )
