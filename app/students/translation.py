from app.students.admin import *
from app.students.models import *
from modeltranslation.translator import translator, TranslationOptions


class ParliamentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ActiveTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class HostelTranslationOptions(TranslationOptions):
    fields = ( 'title', 'description', 
            'accommodation_title', 'accommodation_text', 
            'spiritual_title', 'spiritual_text', 
            'security_title', 'security_text', 
            'student_life_title', 'student_life_text', 
            'reviews_title', 'reviews_text', )


class StudentLifeTranslationOptions(TranslationOptions):
    fields = ( 'title', 'description', 
            'education_title', 'education_text', 
            'spiritual_development_title', 'spiritual_development_text', 
            'cultural_events_title', 'cultural_events_text', 
            'sports_title', 'sports_text', 
            'reviews_title', 'reviews_text')



# Регистрация переводов
translator.register(Parliament, ParliamentTranslationOptions)
translator.register(Active, ActiveTranslationOptions)
translator.register(Hostel, HostelTranslationOptions)
translator.register(StudentLife, StudentLifeTranslationOptions)
