from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.mainpage.views import SettingsAPI

router = DefaultRouter()
router.register('settings', SettingsAPI, basename='settings')

urlpatterns = [
    path('', include(router.urls)),
]
