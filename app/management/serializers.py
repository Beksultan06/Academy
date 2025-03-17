from rest_framework import serializers
from app.management.models import Rector, ScientWorksRector, HR_department, Vacancies, RectorObjectsTitle, ScientWorksRectorObjects, HR_departmentObjects, VacanciesObjects

class RectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rector
        fields = [
            'id',
            'name_rector', 
            'job_title_rector', 
            'education_rector', 
            'image_rector'
        ]
        
class ScientWorksRectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientWorksRector
        fields = [
            'id',
            'description_works', 
            'date_works', 
            'major_works',
            'link_pdf_works',
            'contacs_works',
            'email_works',
            'phone_number_works'
        ]
        
class HR_departmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = HR_department
        fields = [
            'id',
            'name_department',
            'description_department',
            'our_tasks_department', 
            'head_department', 
            'contacs_department',
            'email_department',
            'phone_number_department'
        ]
        
class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = [
            'id',
            'name_vacancy',
            'responsibilities_vacancy',
            'date_vacancy',
            'teacher_islamic_sciences_vacancy',
            'contacs_vacancy',
            'email_vacancy',
            'phone_number_vacancy'
        ]
        
class RectorObjectsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RectorObjectsTitle
        fields = ['id', 'title2', 'rector']
        
class ScientWorksRectorObjectsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ScientWorksRectorObjects
        fields = ['id', 'title2_works', 'scientworks_rector']
        
class HR_departmentObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR_departmentObjects
        fields = ['id', 'title2_department', 'hr_department']
        
class VacanciesObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacanciesObjects
        fields = ['id', 'title2_vacancy', 'vacancy']