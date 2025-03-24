from app.students.admin import *
from app.students.models import *
from modeltranslation.translator import translator, TranslationOptions, register
from . models import Name

@register(ListPages)
class ListPagesTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ListPagesObject)
class ListPagesObjectTranslationOptions(TranslationOptions):
    fields = ('two_title',)
    
@register(Name)
class NameTranslationOptions(TranslationOptions):
    fields = ('title',)

class ParliamentTranslationOptions(TranslationOptions):
    fields = ('students_full_name', 'description')

class PortalTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class Active_StudentsTranslationOptions(TranslationOptions):
    fields = ('students_full_name', 'description')

class HostelTranslationOptions(TranslationOptions):
    fields = ( 'title', 'description')

class StudentLifeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(StudentsLife, StudentLifeTranslationOptions)
translator.register(Parliament, ParliamentTranslationOptions)
translator.register(Active_Students, Active_StudentsTranslationOptions)
translator.register(Hostel, HostelTranslationOptions)
translator.register(Portal, PortalTranslationOptions)
