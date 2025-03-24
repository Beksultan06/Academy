from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from app.students.models import *
from app.students.translation import *  
from django.forms.models import BaseInlineFormSet

class NameAdmin(TranslationAdmin):
    fields = ('title',)

admin.site.register(Name, NameAdmin)

class ParliamentAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('images',),
        }),
        ('Русская версия', {
            'fields': ('students_full_name_ru', 'description_ru'),
        }),
        ('Английская версия', {
            'fields': ('students_full_name_en', 'description_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('students_full_name_ky', 'description_ky'),
        }),
        ('Турецкая версия', {
            'fields': ('students_full_name_tr', 'description_tr'),
        }),
        ('Арабская версия', {
            'fields': ('students_full_name_ar', 'description_ar'),
        }),
    )

class PortalAdmin(TranslationAdmin):
    fieldsets = (
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
        ('Фотография', {
            'fields': ('images',),
        }),
        ('Русская версия', {
            'fields': ('students_full_name_ru', 'description_ru'),
        }),
        ('Английская версия', {
            'fields': ('students_full_name_en', 'description_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('students_full_name_ky', 'description_ky'),
        }),
        ('Турецкая версия', {
            'fields': ('students_full_name_tr', 'description_tr'),
        }),
        ('Арабская версия', {
            'fields': ('students_full_name_ar', 'description_ar'),
        }),
    )

class HostelObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            if 'images' in form.fields:
                form.fields['images'].widget.attrs.update({'style': 'display:none;'})
                form.fields['images'].required = False

class HostelObjectInline(admin.TabularInline):
    model = HostelObject
    formset = HostelObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class HostelAdmin(TranslationAdmin):
    fieldsets = (
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
    inlines = [HostelObjectInline]

class StudentLifeObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            if 'images' in form.fields:
                form.fields['images'].widget.attrs.update({'style': 'display:none;'})
                form.fields['images'].required = False

class StudentLifeObjectInline(admin.TabularInline):
    model = StudentsLifeObject
    formset = StudentLifeObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class StudentLifeAdmin(TranslationAdmin):
    fieldsets = (
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
    inlines = [StudentLifeObjectInline]

class ListPagesObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            for lang in ['ru', 'ky', 'en', 'ar', 'tr']:
                field_name = f'two_title_{lang}'
                if field_name in form.fields:
                    form.fields[field_name].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
                    form.fields[field_name].required = False


class ListPagesObjectInline(admin.TabularInline):
    model = ListPagesObject 
    formset = ListPagesObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

    def get_fieldsets(self, request, obj=None):
        return (
        ('Русская версия', {
            'fields': ['two_title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['two_title_ky'],
        }),
        ('Английский версия', {
            'fields': ['two_title_en'],
        }),
        ('Арабский версия', {
            'fields': ['two_title_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['two_title_tr'],
        }),
    )

class ListPagesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr'],
        }),
    )
    inlines = [ListPagesObjectInline] 

admin.site.register(ListPages, ListPagesAdmin)
admin.site.register(StudentsLife, StudentLifeAdmin)
admin.site.register(Hostel, HostelAdmin)
admin.site.register(Parliament, ParliamentAdmin)
admin.site.register(Active_Students, ActiveAdmin)
