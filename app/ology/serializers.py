from rest_framework import serializers
from .models import AcademicCouncil, ScientificJournals, CenterEducation

class AcademicCouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCouncil
        fields = ['id', 'title', 'description', 'email', 'number']

class ScientificJournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificJournals
        fields = ['id', 'title', 'description', 'image', 'link']

class CenterEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterEducation
        fields = ['id', 'title', 'description', 'email', 'number']
