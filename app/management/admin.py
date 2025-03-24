from django.contrib import admin
from app.management.models import *
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet
from .translation import *

# Register your models here.

class NameAdmin(TranslationAdmin):
    fields = ('title',)

admin.site.register(Name, NameAdmin)

class RectorAdminForm(ModelForm):
    class Meta:
        model = Rector
        fields = '__all__'

class RectorObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2'].required = False

class RectorObjectInline(admin.TabularInline):
    model = RectorObjectsTitle
    formset = RectorObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class RectorAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('name_rector_ru', 'job_title_rector_ru', 'education_rector_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('name_rector_ky', 'job_title_rector_ky', 'education_rector_ky')
        }),
        ("Английская версия", {
            'fields': ('name_rector_en', 'job_title_rector_en', 'education_rector_en')
        }),
        ("Туркская версия", {
            'fields': ('name_rector_tr', 'job_title_rector_tr', 'education_rector_tr')
        }),
        ("Арабская версия", {
            'fields': ('name_rector_ar', 'job_title_rector_ar', 'education_rector_ar')
        }),
        ("Фото ректора", {
            'fields': ('image_rector',)
        }),
    )
    inlines = [RectorObjectInline]

class ScientWorksRectorAdminForm(ModelForm):
    class Meta:
        model = ScientWorksRector
        fields = '__all__'

class ScientWorksRectorObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2_works'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2_works'].required = False

class ScientWorksRectorObjectInline(admin.TabularInline):
    model = ScientWorksRectorObjects
    formset = ScientWorksRectorObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class ScientWorksRectorAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('description_works_ru', 'date_works_ru','major_works_ru', 'contacs_works_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('description_works_ky', 'date_works_ky','major_works_ky', 'contacs_works_ky')
        }),
        ("Английская версия", {
            'fields': ('description_works_en', 'date_works_en','major_works_en', 'contacs_works_en')
        }),
        ("Туркская версия", {
            'fields': ('description_works_tr', 'date_works_tr','major_works_tr', 'contacs_works_tr')
        }),
        ("Арabicская версия", {
            'fields': ('description_works_ar', 'date_works_ar','major_works_ar', 'contacs_works_ar')
        }),
        ("Ссылка на PDF", {
            'fields': ('link_pdf_works',)
        }),
        ("Контакты для связи", {
            'fields': ('email_works', 'phone_number_works')
        })
    )

    inlines = [ScientWorksRectorObjectInline]

class HR_departmentAdminForm(ModelForm):
    class Meta:
        model = HR_department
        fields = '__all__'

class HR_departmentObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2_department'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2_department'].required = False

class HR_departmentObjectInline(admin.TabularInline):
    model = HR_departmentObjects
    formset = HR_departmentObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class HR_departmentAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('name_department_ru', 'contacs_department_ru', 'description_department_ru', 'our_tasks_department_ru', 'head_department_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('name_department_ky', 'contacs_department_ky', 'description_department_ky', 'our_tasks_department_ky', 'head_department_ky',)
        }),
        ("Английская версия", {
            'fields': ('name_department_en', 'contacs_department_en', 'description_department_en', 'our_tasks_department_en', 'head_department_en',)
        }),
        ("Туркская версия", {
            'fields': ('name_department_tr', 'contacs_department_tr', 'description_department_tr', 'our_tasks_department_tr', 'head_department_tr',)
        }),
        ("Арabicская версия", {
            'fields': ('name_department_ar', 'contacs_department_ar', 'description_department_ar', 'our_tasks_department_ar', 'head_department_ar',)
        }),
        ("Контакты для связи", {
            'fields': ('email_department', 'phone_number_department')
        })
    )
    inlines = [HR_departmentObjectInline]

class VacanciesAdminForm(ModelForm):
    class Meta:
        model = Vacancies
        fields = '__all__'

class VacanciesObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2'].required = False

class VacanciesObjectInline(admin.TabularInline):
    model = VacanciesObjects
    formset = VacanciesObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class VacanciesAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('name_vacancy_ru', 'responsibilities_vacancy_ru', 'date_vacancy_ru', 'teacher_islamic_sciences_vacancy_ru', 'contacs_vacancy_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('name_vacancy_ky', 'responsibilities_vacancy_ky', 'date_vacancy_ky', 'teacher_islamic_sciences_vacancy_ky', 'contacs_vacancy_ky')
        }),
        ("Английская версия", {
            'fields': ('name_vacancy_en', 'responsibilities_vacancy_en', 'date_vacancy_en', 'teacher_islamic_sciences_vacancy_en', 'contacs_vacancy_en')
        }),
        ("Туркская версия", {
            'fields': ('name_vacancy_tr', 'responsibilities_vacancy_tr', 'date_vacancy_tr', 'teacher_islamic_sciences_vacancy_tr', 'contacs_vacancy_tr')
        }),
        ("Арabicская версия", {
            'fields': ('name_vacancy_ar', 'responsibilities_vacancy_ar', 'date_vacancy_ar', 'teacher_islamic_sciences_vacancy_ar', 'contacs_vacancy_ar')
        }),
        ("Контакты для связи", {
            'fields': ('email_vacancy', 'phone_number_vacancy')
        })
    )
    inlines = [VacanciesObjectInline]

admin.site.register(Rector, RectorAdmin)
admin.site.register(ScientWorksRector, ScientWorksRectorAdmin)
admin.site.register(HR_department, HR_departmentAdmin)
admin.site.register(Vacancies, VacanciesAdmin)
