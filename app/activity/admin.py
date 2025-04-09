from django.contrib import admin
from app.activity.models import Activity
from modeltranslation.admin import TranslationAdmin
from . translations import *

class ActivityAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru', 'description_ru', 'date_ru', 'title_obj_ru', 'description_obj_ru', 'place_ru', 'link_ru',)
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'description_ky', 'date_ky', 'title_obj_ky', 'description_obj_ky', 'place_ky', 'link_ky',)
        }),
        ("Английская версия", {
            'fields': ('title_en', 'description_en', 'date_en', 'title_obj_en', 'description_obj_en', 'place_en', 'link_en',)
        }),
        ("Туркская версия", {
            'fields': ('title_tr', 'description_tr', 'date_tr', 'title_obj_tr', 'description_obj_tr', 'place_tr', 'link_tr',)
        }),
        ("Арaбская версия", {
            'fields': ('title_ar', 'description_ar', 'date_ar', 'title_obj_ar', 'description_obj_ar', 'place_ar', 'link_ar',)
        }),
        ("Основа", {
            'fields': ("image",)
        })
    )

admin.site.register(Activity, ActivityAdmin)