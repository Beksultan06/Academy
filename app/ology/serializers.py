from rest_framework import serializers
from app.ology.models import Ology

class OlogySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    number = serializers.IntegerField()
    email = serializers.EmailField()
    link = serializers.URLField()

    class Meta:
        model = Ology
        fields = ['id', 'title', 'description', 'number', 'email', 'link']
