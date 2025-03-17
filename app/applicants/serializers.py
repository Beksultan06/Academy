from rest_framework import serializers
from .models import *

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = ['id', 'title', 'description', 'email', 'number']


class Admissions_CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admissions_Committee
        fields = ['id', 'title', 'description', 'email', 'number']