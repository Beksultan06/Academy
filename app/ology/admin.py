from django.contrib import admin
from .models import *
from . translation import *
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet

class NameAdmin(TranslationAdmin):
    fields = ('title',)

admin.site.register(Name, NameAdmin)

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


class ScientificJournalsAdminForm(ModelForm):
    class Meta:
        model = ScientificJournals
        fields = '__all__'

class ScientificJournalsObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['journal'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['journal'].required = False

class ScientificJournalsObjectInline(admin.TabularInline):
    model = ScientificJournalsObject
    formset = ScientificJournalsObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

    
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
    inlines = [ScientificJournalsObjectInline]

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
