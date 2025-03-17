from rest_framework import viewsets, mixins
from .models import (
    Banner, News, Degree, Recommendation, 
    AcademyJournal, PartnerJournal, GalleryImage
)
from .serializers import (
    BannerSerializer, NewsSerializer, DegreeSerializer, 
    RecommendationSerializer, AcademyJournalSerializer, 
    PartnerJournalSerializer, GallerySerializer
)

class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class NewsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class DegreeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer

class RecommendationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class AcademyJournalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    queryset = AcademyJournal.objects.all()
    serializer_class = AcademyJournalSerializer

class PartnerJournalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    queryset = PartnerJournal.objects.all()
    serializer_class = PartnerJournalSerializer

class GalleryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):  
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer
