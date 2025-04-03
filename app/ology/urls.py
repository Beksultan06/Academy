from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'ology', OlogyViewSet, basename='ologys')


urlpatterns = [
    path('', include(router.urls)),  
]
