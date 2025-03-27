from rest_framework import serializers
from .models import *
from django.conf import settings


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id', 'title')
        ref_name = 'MagNameSerializer'


class ParliamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parliament
        fields = ('id', 'students_full_name', 'description', 'images')


class StudentWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWork
        fields = ('name', 'description', 'img')

class ActiveSerializer(serializers.ModelSerializer):
    work = StudentWorkSerializer(many=True, read_only=True)  # Добавляем работы в сериализатор

    class Meta:
        model = Active_Students
        fields = ('id', 'name', 'description', 'descriptions', 'images', 'work')




class Active_StudentsAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Active_StudentsAbout
        fields = ('id', 'title', 'description', 'images')


class HostelSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Hostel
        fields = ('id', 'title', 'description', 'images')

    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.images.all()

        image_urls = []
        for image in images:
            if image.images:
                image_url = image.images.url
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.images}"
                image_urls.append(image_url)

        return image_urls


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = ('id', 'title', 'description', 'contacts')


class StudentsLifeSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = StudentsLife
        fields = ('id', 'title', 'description', 'images')

    def get_images(self, obj):
        request = self.context.get('request')
        images = StudentsLifeObject.objects.filter(hostel=obj)

        image_urls = []
        for image in images:
            if image.images:
                image_url = image.images.url
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.images}"
                image_urls.append(image_url)

        return image_urls


class ListPagesSerializer(serializers.ModelSerializer):
    two_title = serializers.SerializerMethodField()

    class Meta:
        model = ListPages
        fields = ['id', 'title', 'two_title']

    def get_two_title(self, obj):
        return list(obj.listpagesobject_set.values_list('two_title', flat=True))
