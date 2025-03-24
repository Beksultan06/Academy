from rest_framework import serializers
from app.education.models import *


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id', 'title')
        ref_name = 'EducationNameSerializer' 

        
class WelcomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomePage
        fields = ['id', 'title_welcome', 'information_title_welcome', 'information']
        
class EducationMiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationMiddle
        fields = ['id', 'title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education']

class ApeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ape
        fields = ['id', 'title', 'description']

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id','title','description',]

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id','title','description',]
        
class EducationProSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationPro
        fields = ['id', 'title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education']


class EducationSeniorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationSenior
        fields = ['id', 'title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education']


class EducationDoctoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDoctora
        fields = ['id', 'title_education', 'description_education', 'title_facult_education', 'description_facult_education', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education']

class WelcomePageObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomePageObjects
        fields = ['id', 'title2_object']
        
class EducationMiddleObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationMiddleObjects
        fields = ['id', 'title2_object']
        

class EducationDoctoraObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDoctoraObjects
        fields = ['id', 'title_object']
    
class EducationSeniorObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationSeniorObjects
        fields = ['id', 'title_object']
        
class EducationProObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationProObjects
        fields = ['id', 'title2_object']
