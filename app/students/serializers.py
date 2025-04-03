from rest_framework import serializers
from .models import ScientificJournal, ScientificJournalObject

class ScientificJournalObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificJournalObject
        fields = ['id', 'image']

class ScientificJournalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    students_full_name = serializers.CharField()
    images = ScientificJournalObjectSerializer(many=True, read_only=True, source='scientificjournalobject_set')

    class Meta:
        model = ScientificJournal
        fields = ['id', 'title', 'description', 'students_full_name', 'number', 'email', 'link', 'images']
