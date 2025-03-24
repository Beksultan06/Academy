from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from . translation import *
from app.education.models import *
from django.forms import BaseInlineFormSet
from app.education.models import *
from modeltranslation.admin import TranslationAdmin
from . translation import *
from django.forms import ModelForm, BaseInlineFormSet

# Register your models here.

class NameAdmin(TranslationAdmin):
    fields = ('title',)

admin.site.register(Name, NameAdmin)

class WelcomePageAdminForm(ModelForm):
    class Meta:
        model = WelcomePage
        fields = '__all__'

class WelcomePageObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title_welcome'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title_welcome'].required = False

class WelcomePageObjectInline(admin.TabularInline):
    model = WelcomePageObjects
    formset = WelcomePageObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class WelcomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_welcome_ru', 'information_title_welcome_ru', 'information_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_welcome_ky', 'information_title_welcome_ky', 'information_ky'],
        }),
        ('Английская версия', {
            'fields': ['title_welcome_en', 'information_title_welcome_en', 'information_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_welcome_ar', 'information_title_welcome_ar', 'information_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_welcome_tr', 'information_title_welcome_tr', 'information_tr'],
        })
    )
    inlines = [WelcomePageObjectInline]
    
class EducationMiddleAdminForm(ModelForm):
    class Meta:
        model = EducationMiddle
        fields = '__all__'

class EducationMiddleObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2_object'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2_object'].required = False

class EducationMiddleObjectInline(admin.TabularInline):
    model = EducationMiddleObjects
    formset = EducationMiddleObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs 
    
class EducationMiddleAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_education_ru', 'description_education_ru', 'title_facult_education_ru', 'description_facult_education_ru', 'name_speciality_education_ru', 'status_education_ru', 'form_education_ru', 'perioud_education_ru'],
        }),
        ("Кыргызская версия", {
            'fields': ['title_education_ky', 'description_education_ky', 'title_facult_education_ky', 'description_facult_education_ky', 'name_speciality_education_ky', 'status_education_ky', 'form_education_ky', 'perioud_education_ky'],
        }),
        ("Английская версия", {
            'fields': ['title_education_en', 'description_education_en', 'title_facult_education_en', 'description_facult_education_en', 'name_speciality_education_en', 'status_education_en', 'form_education_en', 'perioud_education_en'],
        }),
        ("Арабсский версия", {
            'fields': ['title_education_ar', 'description_education_ar', 'title_facult_education_ar', 'description_facult_education_ar', 'name_speciality_education_ar', 'status_education_ar', 'form_education_ar', 'perioud_education_ar'],
        }),
        ("Турецкий версия", {
            'fields': ['title_education_tr', 'description_education_tr', 'title_facult_education_tr', 'description_facult_education_tr', 'name_speciality_education_tr', 'status_education_tr', 'form_education_tr', 'perioud_education_tr'],
        })
    )
    inlines = [EducationMiddleObjectInline]
    

admin.site.register(WelcomePage, WelcomePageAdmin)
admin.site.register(EducationMiddle, EducationMiddleAdmin)

#Ape - Дополнительное Профессиональная Образование
class CoursesObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title_object'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title_object'].required = False

class CoursesObjectInline(admin.TabularInline):
    model = CoursesObjects
    formset = CoursesObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class CoursesAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_ru', 'description_ru'],
        }),
        ("Кыргызская версия", {
            'fields': ['title_ky', 'description_ky'],
        }),
        ("Английская версия", {
            'fields': ['title_en', 'description_en'],
        }),
        ("Арабская версия", {
            'fields': ['title_ar', 'description_ar'],
        }),
        ("Турецкая версия", {
            'fields': ['title_tr', 'description_tr'],
        })
    )
    inlines = [CoursesObjectInline]

admin.site.register(Courses, CoursesAdmin)

class ApeObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title_object'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title_object'].required = False

class ApeObjectInline(admin.TabularInline):
    model = ApeObjects
    formset = ApeObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class ApeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_ru', 'description_ru'],
        }),
        ("Кыргызская версия", {
            'fields': ['title_ky', 'description_ky'],
        }),
        ("Английская версия", {
            'fields': ['title_en', 'description_en'],
        }),
        ("Арабская версия", {
            'fields': ['title_ar', 'description_ar'],
        }),
        ("Турецкая версия", {
            'fields': ['title_tr', 'description_tr'],
        })
    )
    inlines = [ApeObjectInline]

admin.site.register(Ape, ApeAdmin)



class LibraryObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title_object'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title_object'].required = False

class LibraryObjectInline(admin.TabularInline):
    model = LibraryObjects
    formset = LibraryObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

class LibraryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_ru', 'description_ru'],
        }),
        ("Кыргызская версия", {
            'fields': ['title_ky', 'description_ky'],
        }),
        ("Английская версия", {
            'fields': ['title_en', 'description_en'],
        }),
        ("Арабская версия", {
            'fields': ['title_ar', 'description_ar'],
        }),
        ("Турецкая версия", {
            'fields': ['title_tr', 'description_tr'],
        })
    )
    inlines = [LibraryObjectInline]

admin.site.register(Library, LibraryAdmin)

# Register your models here.


class EducationProObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2_object'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2_object'].required = False


class EducationProObjectInline(admin.TabularInline):
    model = EducationProObjects
    formset = EducationProObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs


class EducationProAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_education_ru', 'description_education_ru', 'title_facult_education_ru', 'description_facult_education_ru', 'name_speciality_education_ru', 'status_education_ru', 'form_education_ru', 'perioud_education_ru'],
        }),
        ("Кыргызская версия", {
            'fields': ['title_education_ky', 'description_education_ky', 'title_facult_education_ky', 'description_facult_education_ky', 'name_speciality_education_ky', 'status_education_ky', 'form_education_ky', 'perioud_education_ky'],
        }),
        ("Английская версия", {
            'fields': ['title_education_en', 'description_education_en', 'title_facult_education_en', 'description_facult_education_en', 'name_speciality_education_en', 'status_education_en', 'form_education_en', 'perioud_education_en'],
        }),
        ("Арабская версия", {
            'fields': ['title_education_ar', 'description_education_ar', 'title_facult_education_ar', 'description_facult_education_ar', 'name_speciality_education_ar', 'status_education_ar', 'form_education_ar', 'perioud_education_ar'],
        }),
        ("Турецкая версия", {
            'fields': ['title_education_tr', 'description_education_tr', 'title_facult_education_tr', 'description_facult_education_tr', 'name_speciality_education_tr', 'status_education_tr', 'form_education_tr', 'perioud_education_tr'],
        })
    )
    inlines = [EducationProObjectInline]

admin.site.register(EducationPro, EducationProAdmin)



class EducationSeniorObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2_object'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2_object'].required = False


class EducationSeniorObjectInline(admin.TabularInline):
    model = EducationSeniorObjects
    formset = EducationSeniorObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs


class EducationSeniorAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_education_ru', 'description_education_ru', 'title_facult_education_ru', 'description_facult_education_ru', 'name_speciality_education_ru', 'status_education_ru', 'form_education_ru', 'perioud_education_ru'],
        }),
        ("Кыргызская версия", {
            'fields': ['title_education_ky', 'description_education_ky', 'title_facult_education_ky', 'description_facult_education_ky', 'name_speciality_education_ky', 'status_education_ky', 'form_education_ky', 'perioud_education_ky'],
        }),
        ("Английская версия", {
            'fields': ['title_education_en', 'description_education_en', 'title_facult_education_en', 'description_facult_education_en', 'name_speciality_education_en', 'status_education_en', 'form_education_en', 'perioud_education_en'],
        }),
        ("Арабская версия", {
            'fields': ['title_education_ar', 'description_education_ar', 'title_facult_education_ar', 'description_facult_education_ar', 'name_speciality_education_ar', 'status_education_ar', 'form_education_ar', 'perioud_education_ar'],
        }),
        ("Турецкая версия", {
            'fields': ['title_education_tr', 'description_education_tr', 'title_facult_education_tr', 'description_facult_education_tr', 'name_speciality_education_tr', 'status_education_tr', 'form_education_tr', 'perioud_education_tr'],
        })
    )
    inlines = [EducationSeniorObjectInline]

admin.site.register(EducationSenior, EducationSeniorAdmin)




class EducationDoctoraObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['title2_object'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['title2_object'].required = False


class EducationDoctoraObjectInline(admin.TabularInline):
    model = EducationDoctoraObjects
    formset = EducationDoctoraObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs


class EducationDoctoraAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ['title_education_ru', 'description_education_ru', 'title_facult_education_ru', 'description_facult_education_ru', 'name_speciality_education_ru', 'status_education_ru', 'form_education_ru', 'perioud_education_ru'],
        }),
        ("Кыргызская версия", {
            'fields': ['title_education_ky', 'description_education_ky', 'title_facult_education_ky', 'description_facult_education_ky', 'name_speciality_education_ky', 'status_education_ky', 'form_education_ky', 'perioud_education_ky'],
        }),
        ("Английская версия", {
            'fields': ['title_education_en', 'description_education_en', 'title_facult_education_en', 'description_facult_education_en', 'name_speciality_education_en', 'status_education_en', 'form_education_en', 'perioud_education_en'],
        }),
        ("Арабская версия", {
            'fields': ['title_education_ar', 'description_education_ar', 'title_facult_education_ar', 'description_facult_education_ar', 'name_speciality_education_ar', 'status_education_ar', 'form_education_ar', 'perioud_education_ar'],
        }),
        ("Турецкая версия", {
            'fields': ['title_education_tr', 'description_education_tr', 'title_facult_education_tr', 'description_facult_education_tr', 'name_speciality_education_tr', 'status_education_tr', 'form_education_tr', 'perioud_education_tr'],
        })
    )
    inlines = [EducationDoctoraObjectInline]

admin.site.register(EducationDoctora, EducationDoctoraAdmin)