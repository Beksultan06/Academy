from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('search/', GlobalSearchView.as_view(), name='global-search'),  
]
