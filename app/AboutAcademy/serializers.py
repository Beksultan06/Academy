from rest_framework import serializers
from app.AboutAcademy.models import *

class AboutImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutImage
        fields = ['image']

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if obj.image else None

class AboutSerializer(serializers.ModelSerializer):
    images = AboutImageSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = [
            'page_key',
            'title_main',
            'title2',
            'title_page',
            'description',
            'addresses',
            'links_carta',
            'title_pdf',
            'url_pdf',
            'dowl_url',
            'images'
        ]
