from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'name', NameAPI, basename='name')
router.register(r"scientific_objects", ScientificJournalsObjectAPI, basename='scientific_object')
router.register(r'academic_councils', AcademicCouncilAPI, basename='academic_council')
router.register(r'scientific_journals', ScientificJournalsAPI, basename='scientific_journals')
router.register(r'center_education', CenterEducationAPI, basename='center_education')

urlpatterns = [
    path('', include(router.urls)),  
]
