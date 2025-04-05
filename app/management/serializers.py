from rest_framework import serializers
from .models import *

class LeadershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipType
        fields = ['code', 'name']

class LeadershipSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field="code", read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Leadership
        fields = [
            'id',
            'type',
            'title',
            'name',
            'description',
            'image',
            'link',
            'email',
            'phone',
            'contact',
            'responsibilities',
            'date_publication',
        ]

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None
