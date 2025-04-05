from rest_framework import serializers
from .models import Academic

class AcademicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()  
    description = serializers.CharField()  
    number = serializers.CharField()  
    email = serializers.EmailField()  

    class Meta:
        model = Academic
        fields = ['id', 'title', 'description', 'number', 'email']
