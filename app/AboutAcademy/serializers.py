from rest_framework import serializers
from .models import Document
from rest_framework import serializers
from app.AboutAcademy.models import *
from django.conf import settings
from django.urls import reverse

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'description', 'title_phone_number', 'phone_number', 'title_adress', 'adress', 'title_operating_mode', 'operating_mode', 'link_map']
    
class DevStrategySerializers(serializers.ModelSerializer):
    class Meta:
        model = DevStrategy
        fields = ['id', 'title', 'description']

class DevStrategyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevStrategyPhoto
        fields = ['id', 'photo']

class MissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id', 'title', 'description']


class DocumentSerializer(serializers.ModelSerializer):
    open_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'file', 'open_url', 'download_url']

from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    open_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'file', 'open_url', 'download_url']

    def get_open_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url 

    def get_download_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/ru/api/v1/AboutAcademy/document/{obj.id}/download/')
        return f'/ru/api/v1/AboutAcademy/document/{obj.id}/download/'


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ['id', 'title', 'description']

class HistorySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ['id', 'title', 'description', 'images']

    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.historyobject_set.all()

        image_urls = []
        for image in images:
            if image.image:
                image_url = image.image.url
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.image}"
                image_urls.append(image_url)

        return image_urls

class ListPagesSerializer(serializers.ModelSerializer):
    two_title = serializers.SerializerMethodField()

    class Meta:
        model = ListPages
        fields = ['id', 'title', 'two_title']

    def get_two_title(self, obj):
        return list(obj.listpagesobject_set.values_list('two_title', flat=True))
    