from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotosViewSet

router = DefaultRouter()
router.register(r'photos', PhotosViewSet, basename='photos')

urlpatterns = [
    path('', include(router.urls)),
]
