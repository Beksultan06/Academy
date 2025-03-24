from django.urls import path
from rest_framework.routers import DefaultRouter
from app.education.views import *

router = DefaultRouter()
router.register(r'name', NameAPI, basename='name')
router.register(r'welcomepage', WelcomePageViewSet, basename="welcomepage")
router.register(r'educationmiddle', EducationMiddleViewSet, basename="educationmiddle")
router.register(r'ape', ApeAPI, basename='ape')
router.register(r'courses', ApeAPI, basename='courses')
router.register(r'library', ApeAPI, basename='library')
router.register(r'welcomepageobjects', WelcomePageObjectsViewSet, basename="welcomepageobjects")
router.register(r'educationmiddleobjects', EducationMiddleObjectsViewSet, basename="educationmiddleobjects")
router.register(r'education_pro', EducationProViewSet, basename='education_pro')
router.register(r'education_pro_objects', EducationProViewSet, basename='education_pro_objects')  # replace with actual viewset for pro objects
router.register(r'education_senior', EducationSeniorViewSet, basename='education_senior')
router.register(r'education_senior_objects', EducationSeniorViewSet, basename='education_senior_objects')  # replace with actual viewset for senior objects
router.register(r'education_doctora', EducationDoctoraViewSet, basename='education_doctora')
router.register(r'education_doctora_objects', EducationDoctoraObjectsViewSet, basename='education_doctora_objects')


urlpatterns = [
    path('welcomepage/int:pk/', WelcomePageObjectsViewSet.as_view({'get': 'retrieve'}), name="welcomepage"),
    path('educationmiddle/int:pk/', EducationMiddleObjectsViewSet.as_view({'get': 'retrieve'}), name="educationmiddle"),
    path('ape/int:pk/', ApeAPI.as_view({'get':'retrieve'}), name="ape"),
    path('courses/int:pk/', ApeAPI.as_view({'get':'retrieve'}), name="courses"),
    path('library/int:pk/', ApeAPI.as_view({'get':'retrieve'}), name="library"),  # replace with actual viewset for library objects
    path('welcomepageobjects/int:pk/', WelcomePageObjectsViewSet.as_view({'get':'retrieve'}), name="welcomepageobjects"),
    path('educationmiddleobjects/int:pk/', EducationMiddleObjectsViewSet.as_view({'get':'retrieve'}), name="educationmiddleobjects"),
    path('education_pro/int:pk/', EducationProViewSet.as_view({'get':'retrieve'}), name="education_pro"),
    path('education_senior/int:pk/', EducationSeniorViewSet.as_view({'get':'retrieve'}), name="education_senior"),
    path('education_doctora/int:pk/', EducationDoctoraViewSet.as_view({'get':'retrieve'}), name="education_doctora"),
    path('education_doctora_objects/int:pk/', EducationDoctoraObjectsViewSet.as_view({'get':'retrieve'}), name="education_doctora_objects"),  # replace with actual viewset for education doctora objects
    path('base', NameAPI.as_view, name='names'),
]

urlpatterns += router.urls


