from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet
from .models import *
from . translation import *


class AllEducationAdminForm(ModelForm):
    class Meta:
        model = AllEducation
        fields = '__all__'


class AllEducationObjectInline(admin.TabularInline):  # Можно заменить на admin.StackedInline
    model = AllEducationObject
    extra = 1  # Количество пустых полей для добавления новых объектов
    verbose_name = "Объект образования"
    verbose_name_plural = "Объекты образования"


class AllEducationAdmin(TranslationAdmin):
    form = AllEducationAdminForm
    inlines = [AllEducationObjectInline]

    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru', 'description_ru'),
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'description_ky')
        }),
        ("Английская версия", {
            'fields': ('title_en', 'description_en',)
        }),
        ("Туркская версия", {
            'fields': ('title_tr', 'description_tr')
        }),
        ("Арабская версия", {
            'fields': ('title_ar', 'description_ar')
        }),
    )


admin.site.register(AllEducation, AllEducationAdmin)
