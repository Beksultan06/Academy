from django.contrib import admin
from .models import *
from .translation import *
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet

class ScientificJournalAdminForm(ModelForm):
    class Meta:
        model = ScientificJournal
        fields = '__all__'

class ScientificJournalObjectInline(admin.TabularInline):
    model = ScientificJournalObject
    extra = 1

class ScientificJournalsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'students_full_name_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'students_full_name_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_en', 'description_en', 'students_full_name_en'],
        }),
        ('Арабская версия', {
            'fields': ['title_ar', 'description_ar', 'students_full_name_ar'],
        }),
        ('Турецкая версия', {
            'fields': ['title_tr', 'description_tr', 'students_full_name_tr'],
        }),
        ('Global', {
            'fields': ['number', 'email', 'link'],
        }),
    )
    inlines = [ScientificJournalObjectInline]

admin.site.register(ScientificJournal, ScientificJournalsAdmin)
