from rest_framework import serializers
from app.activity.models import Progress, AllProgress, Educational

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = [
            'id',
            'title', 
            'description'
        ]
        
class AllProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllProgress
        fields = [
            'id',
            'date', 
            'awarded',
            'achieve',
            'location',
            'image',    
        ]
    
class EducationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educational
        fields = [
            'id',
            'title'
            'date', 
            'awarded', 
            'achieve',
            'location',
            'image',    
        ]
        