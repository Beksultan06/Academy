from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BannerViewSet, NewsViewSet, DegreeViewSet, RecommendationViewSet, 
    AcademyJournalViewSet, PartnerJournalViewSet, GalleryViewSet
)

router = DefaultRouter()
router.register(r'banner', BannerViewSet, basename='banner')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'degrees', DegreeViewSet, basename='degrees')
router.register(r'recommendations', RecommendationViewSet, basename='recommendations')
router.register(r'academy-journals', AcademyJournalViewSet, basename='academy-journals')
router.register(r'partner-journals', PartnerJournalViewSet, basename='partner-journals')
router.register(r'gallery', GalleryViewSet, basename='gallery')

urlpatterns = [
    path('', include(router.urls)),
]
