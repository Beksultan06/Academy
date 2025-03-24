from django.contrib import admin
from app.activity.models import *
from modeltranslation.admin import TranslationAdmin
from . translations import *

class NameAdmin(TranslationAdmin):
    fields = ('title',)

admin.site.register(Name, NameAdmin)

class ProgressAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru', 'description_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'description_ky',)
        }),
        ("Английская версия", {
            'fields': ('title_en', 'description_en')
        }),
        ("Туркская версия", {
            'fields': ('title_tr', 'description_tr')
        }),
        ("Арaбская версия", {
            'fields': ('title_ar', 'description_ar')
        })
    )

admin.site.register(Progress, ProgressAdmin)


class AllProgressAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('awarded_ru', 'achieve_ru', 'location_ru', 'date_ru',)
        }),
        ("Кыргызская версия", {
            'fields': ('awarded_ky', 'achieve_ky', 'location_ky', 'date_ky',)
        }),
        ("Английская версия", {
            'fields': ('awarded_en', 'achieve_en', 'location_en', 'date_en',)
        }),
        ("Туркская версия", {
            'fields': ('awarded_tr', 'achieve_tr', 'location_tr', 'date_tr',)
        }),
        ("Арaбская версия", {
            'fields': ('awarded_ar', 'achieve_ar', 'location_ar', 'date_ar',)
        }),
        ("Global", {
            'fields': ('image',)  
        })
    )

admin.site.register(AllProgress, AllProgressAdmin)

class EducationalAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru','awarded_ru', 'achieve_ru', 'location_ru', 'date_ru',)
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'awarded_ky', 'achieve_ky', 'location_ky', 'date_ky',)
        }),
        ("Английская версия", {
            'fields': ('title_en', 'awarded_en', 'achieve_en', 'location_en', 'date_en',)
        }),
        ("Туркская версия", {
            'fields': ('title_tr', 'awarded_tr', 'achieve_tr', 'location_tr', 'date_tr',)
        }),
        ("Арaбская версия", {
            'fields': ('title_ar', 'awarded_ar', 'achieve_ar', 'location_ar', 'date_ar',)
        }),
        ("Глобальные", {
            'fields': ('image',)  
        })
    )

admin.site.register(Educational, EducationalAdmin)