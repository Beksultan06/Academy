from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcademicViewSet

router = DefaultRouter()
router.register(r'academic_councils', AcademicViewSet, basename='academic_council')


urlpatterns = [
    path('', include(router.urls)),  
]