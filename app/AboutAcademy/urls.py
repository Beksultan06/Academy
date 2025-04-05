from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.AboutAcademy.views import *

router = DefaultRouter()
router.register(r'about', AboutViewSet, basename='about')

urlpatterns = [
    path('', include(router.urls)),
]