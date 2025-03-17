from rest_framework import serializers
from .models import Parliament, Active, Hostel, StudentLife

class ParliamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parliament
        fields = ('title', 'description', 'images')

class ActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Active
        fields = ('title', 'description', 'images')


from rest_framework import serializers
from .models import Hostel, StudentLife

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = (
            'title', 'description', 
            'accommodation_title', 'accommodation_text', 
            'spiritual_title', 'spiritual_text', 
            'security_title', 'security_text', 
            'student_life_title', 'student_life_text', 
            'reviews_title', 'reviews_text', 
            'images'
        )

class StudentLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLife
        fields = (
            'title', 'description', 
            'education_title', 'education_text', 
            'spiritual_development_title', 'spiritual_development_text', 
            'cultural_events_title', 'cultural_events_text', 
            'sports_title', 'sports_text', 
            'reviews_title', 'reviews_text', 
            'images'
        )
