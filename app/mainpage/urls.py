from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.mainpage.views import SettingsAPI, NewsMainViewSet, MagazineViewSet

router = DefaultRouter()
router.register('settings', SettingsAPI, basename='settings')
router.register(r'news', NewsMainViewSet, basename='news')
router.register(r'magazine', MagazineViewSet, basename='magazine')

urlpatterns = [
    path('', include(router.urls)),
]
