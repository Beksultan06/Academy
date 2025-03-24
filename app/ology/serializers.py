from rest_framework import serializers
from .models import *

class ScientificJournalsObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificJournalsObject
        fields = ['id', 'title2_object',]


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id', 'title')
        ref_name = 'OlogyNameSerializer'


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
