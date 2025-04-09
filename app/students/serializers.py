from rest_framework import serializers
from .models import ScientificJournal, ScientificJournalObject, ScientificJournalWork

class ScientificJournalObjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ScientificJournalObject
        fields = ['id', 'image']

class ScientificJournalWorkSerializer(serializers.ModelSerializer):
    img = serializers.ImageField()

    class Meta:
        model = ScientificJournalWork
        fields = ['name', 'description', 'img']

class ScientificJournalSerializer(serializers.ModelSerializer):
    images = ScientificJournalObjectSerializer(many=True, source='scientificjournalobject_set')
    work = ScientificJournalWorkSerializer(many=True, source='works')

    class Meta:
        model = ScientificJournal
        fields = ['id', 'title', 'description', 'images', 'work']
