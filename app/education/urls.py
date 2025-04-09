from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'alleducation', AllEducationViewSet, basename='alleducation')
#router.register(r'xxxxxxx', AllEducationViewSet, basename='xxxxxxxxx')


urlpatterns = [
    path('', include(router.urls)),
]
