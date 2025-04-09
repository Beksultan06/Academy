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

class ScientificJournalWorkForm(ModelForm):
    class Meta:
        model = ScientificJournalWork
        fields = '__all__'

class ScientificJournalWorkInline(admin.TabularInline):
    model = ScientificJournalWork
    extra = 1



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
    )
    inlines = [ScientificJournalObjectInline, ScientificJournalWorkInline]
    

admin.site.register(ScientificJournal, ScientificJournalsAdmin)
