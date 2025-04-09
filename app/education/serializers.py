from rest_framework import serializers
from .models import AllEducation, AllEducationObject

class AllEducationObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllEducationObject
        fields = [
            'id', 'name_speciality_education', 'status_education', 'form_education', 'perioud_education'
        ]

class AllEducationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    objects_education = AllEducationObjectSerializer(many=True, source='alleducationobject_set', read_only=True)

    class Meta:
        model = AllEducation
        fields = [
            'id', 'title', 'description', 'objects_education'
        ]
