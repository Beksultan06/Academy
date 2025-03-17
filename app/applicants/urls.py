from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcademicAPI, Admissions_CommitteeAPI

router = DefaultRouter()
router.register(r'academic_councils', AcademicAPI, basename='academic_council')
router.register(r'/admissions_committee', Admissions_CommitteeAPI, basename='admissions_committee')

urlpatterns = [
    path('', include(router.urls)),  
]