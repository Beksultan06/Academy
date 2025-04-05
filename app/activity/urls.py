from django.urls import path
from app.activity.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activity', ActivityViewSet, basename="activity")

urlpatterns = [
    
]
urlpatterns += router.urls