from modeltranslation.translator import translator, TranslationOptions, register
from modeltranslation.fields import TranslationField
from app.management.models import Rector, ScientWorksRector, HR_department, Vacancies, RectorObjectsTitle, ScientWorksRectorObjects, VacanciesObjects, HR_departmentObjects


@register(Rector)
class RectorTranslationOptions(TranslationOptions):
    fields = ('name_rector', 'job_title_rector', 'education_rector')

@register(ScientWorksRector)
class ScientWorksRectorTranslationOptions(TranslationOptions):
    fields = ('description_works', 'date_works', 'major_works', 'contacs_works')

@register(HR_department)
class HR_departmentTranslationOptions(TranslationOptions):
    fields = ('name_department', 'description_department', 'our_tasks_department', 'head_department', 'contacs_department')

@register(Vacancies)
class VacanciesTranslationOptions(TranslationOptions):
    fields = ('name_vacancy', 'responsibilities_vacancy', 'date_vacancy', 'teacher_islamic_sciences_vacancy', 'contacs_vacancy')
    
@register(RectorObjectsTitle)
class RectorObjectsTitleTranslationOptions(TranslationOptions):
    fields = ('title2',)
    
@register(ScientWorksRectorObjects)
class ScientWorksRectorObjectsTranslationOptions(TranslationOptions):
    fields = ('title2_works',)

@register(VacanciesObjects)
class VacanciesObjectsTranslationOptions(TranslationOptions):
    fields = ('title2_vacancy',)
    
@register(HR_departmentObjects)
class HR_departmentObjectsTranslationOptions(TranslationOptions):
    fields = ('title2_department',)