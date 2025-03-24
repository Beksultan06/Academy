from django.urls import path
from app.activity.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'name', NameAPI, basename='name')
router.register(r'Progress', ProgressViewSet, basename="Progress")
router.register(r'AllProgress', AllProgressViewSet, basename="AllProgress")
router.register(r'Educational', EducationalViewSet, basename="Educational")

urlpatterns = [
    
]
urlpatterns += router.urls