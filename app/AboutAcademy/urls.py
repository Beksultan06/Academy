from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.AboutAcademy.views import *

router = DefaultRouter()
router.register(r'/aboutus', AboutUsAPI, basename='aboutus')
router.register(r'/devstrategy', DevStrategyAPI, basename='devstrategy')
router.register(r'/devstrategyPhoto', DevStrategyPhotoAPI, basename='devstrategyphoto')
router.register(r'/mission', MissionAPI, basename='mission')
router.register(r'/document', DocumentAPI, basename='Document')
router.register(r'/achievements', AchievementsAPI, basename='achievements')
router.register(r'/history', HistoryAPI, basename='history')
router.register(r'/listpagesabout', ListPagesAPI, basename='listpagesabout')


urlpatterns = [
    path('', include(router.urls)),
    path('/document/<int:pk>/', DocumentAPI.as_view({'get': 'retrieve'}), name='media_detail'),
]