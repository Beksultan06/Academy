from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from app.students.models import Parliament, Active, Hostel, StudentLife
from app.students.translation import *  

class ParliamentAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('images',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'description_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'description_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'description_ky'),
        }),
        ('Турецкая версия', {
            'fields': ('title_tr', 'description_tr'),
        }),
        ('Арабская версия', {
            'fields': ('title_ar', 'description_ar'),
        }),
    )

class ActiveAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('images',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'description_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'description_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'description_ky'),
        }),
        ('Турецкая версия', {
            'fields': ('title_tr', 'description_tr'),
        }),
        ('Арабская версия', {
            'fields': ('title_ar', 'description_ar'),
        }),
    )

class HostelAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('images',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'description_ru', 'accommodation_title_ru', 'accommodation_text_ru', 
                       'spiritual_title_ru', 'spiritual_text_ru', 'security_title_ru', 'security_text_ru', 
                       'student_life_title_ru', 'student_life_text_ru', 'reviews_title_ru', 'reviews_text_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'description_en', 'accommodation_title_en', 'accommodation_text_en',
                       'spiritual_title_en', 'spiritual_text_en', 'security_title_en', 'security_text_en',
                       'student_life_title_en', 'student_life_text_en', 'reviews_title_en', 'reviews_text_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'description_ky', 'accommodation_title_ky', 'accommodation_text_ky',
                       'spiritual_title_ky', 'spiritual_text_ky', 'security_title_ky', 'security_text_ky',
                       'student_life_title_ky', 'student_life_text_ky', 'reviews_title_ky', 'reviews_text_ky'),
        }),
        ('Турецкая версия', {
            'fields': ('title_tr', 'description_tr', 'accommodation_title_tr', 'accommodation_text_tr',
                       'spiritual_title_tr', 'spiritual_text_tr', 'security_title_tr', 'security_text_tr',
                       'student_life_title_tr', 'student_life_text_tr', 'reviews_title_tr', 'reviews_text_tr'),
        }),
        ('Арабская версия', {
            'fields': ('title_ar', 'description_ar', 'accommodation_title_ar', 'accommodation_text_ar',
                       'spiritual_title_ar', 'spiritual_text_ar', 'security_title_ar', 'security_text_ar',
                       'student_life_title_ar', 'student_life_text_ar', 'reviews_title_ar', 'reviews_text_ar'),
        }),
    )

class StudentLifeAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('images',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'description_ru', 'education_title_ru', 'education_text_ru',
                       'spiritual_development_title_ru', 'spiritual_development_text_ru', 'cultural_events_title_ru', 
                       'cultural_events_text_ru', 'sports_title_ru', 'sports_text_ru', 'reviews_title_ru', 'reviews_text_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'description_en', 'education_title_en', 'education_text_en',
                       'spiritual_development_title_en', 'spiritual_development_text_en', 'cultural_events_title_en', 
                       'cultural_events_text_en', 'sports_title_en', 'sports_text_en', 'reviews_title_en', 'reviews_text_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'description_ky', 'education_title_ky', 'education_text_ky',
                       'spiritual_development_title_ky', 'spiritual_development_text_ky', 'cultural_events_title_ky', 
                       'cultural_events_text_ky', 'sports_title_ky', 'sports_text_ky', 'reviews_title_ky', 'reviews_text_ky'),
        }),
        ('Турецкая версия', {
            'fields': ('title_tr', 'description_tr', 'education_title_tr', 'education_text_tr',
                       'spiritual_development_title_tr', 'spiritual_development_text_tr', 'cultural_events_title_tr', 
                       'cultural_events_text_tr', 'sports_title_tr', 'sports_text_tr', 'reviews_title_tr', 'reviews_text_tr'),
        }),
        ('Арабская версия', {
            'fields': ('title_ar', 'description_ar', 'education_title_ar', 'education_text_ar',
                       'spiritual_development_title_ar', 'spiritual_development_text_ar', 'cultural_events_title_ar', 
                       'cultural_events_text_ar', 'sports_title_ar', 'sports_text_ar', 'reviews_title_ar', 'reviews_text_ar'),
        }),
    )

admin.site.register(Parliament, ParliamentAdmin)
admin.site.register(Active, ActiveAdmin)
admin.site.register(Hostel, HostelAdmin)
admin.site.register(StudentLife, StudentLifeAdmin)
