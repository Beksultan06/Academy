from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import (
    Banner, News, Degree, Recommendation, 
    AcademyJournal, PartnerJournal, GalleryImage
)

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'

class AcademyJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademyJournal
        fields = '__all__'

class PartnerJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerJournal
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'
