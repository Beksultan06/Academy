from django.contrib import admin
from app.AboutAcademy.models import *
from app.AboutAcademy.translation import *
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet

# Register your models here.

class NameAdmin(TranslationAdmin):
    fields = ('title',)

admin.site.register(Name, NameAdmin)



class AboutUsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru',  'title_phone_number_ru', 'phone_number_ru', 'title_adress_ru', 'adress_ru', 'title_operating_mode_ru', 'operating_mode_ru', 'link_map_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky',  'title_adress_ky', 'adress_ky', 'title_operating_mode_ky', 'operating_mode_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en',  'title_adress_en', 'adress_en', 'title_operating_mode_en', 'operating_mode_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar',  'title_adress_ar', 'adress_ar', 'title_operating_mode_ar', 'operating_mode_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr',  'title_adress_tr', 'adress_tr', 'title_operating_mode_tr', 'operating_mode_tr'],
        }),
    )
admin.site.register(AboutUs, AboutUsAdmin)

class DevStrategyAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
admin.site.register(DevStrategy, DevStrategyAdmin)


class MissionAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
admin.site.register(Mission, MissionAdmin)

class DocumentAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'title_2_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'title_2_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'title_2_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'title_2_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'title_2_tr'],
        }),
        ('File', {
            'fields': ['file'],
        }),
    )

admin.site.register(Document, DocumentAdmin)



class AchievementsObjectForm(ModelForm):
    class Meta:
        model = AchievementsObject
        fields = '__all__'


class AchievementsObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['image'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['image'].required = False


class AchievementsObjectInline(admin.TabularInline):
    model = AchievementsObject
    form = AchievementsObjectForm
    formset = AchievementsObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)

        return qs

    def get_fieldsets(self, request, obj=None):
        return (
            ('Изображение', {
                'fields': ('image',),
            }),
        )


class AchievementsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
    inlines = [AchievementsObjectInline]


admin.site.register(Achievements, AchievementsAdmin)









#####################################################################
class HistoryObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['image'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['image'].required = False

class NewsObjectInline(admin.TabularInline):
    model = HistoryObject 
    formset = HistoryObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

    def get_fieldsets(self, request, obj=None):
        return (
            ('Изображение', {
                'fields': ('image',),
            }),
        )
    
class HistoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
    inlines = [NewsObjectInline] 

admin.site.register(History, HistoryAdmin)

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