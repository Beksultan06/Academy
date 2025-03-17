from django.urls import path
from rest_framework.routers import DefaultRouter
from app.education.views import *

router = DefaultRouter()
router.register(r'welcomepage', WelcomePageViewSet, basename="welcomepage")
router.register(r'educationmiddle', EducationMiddleViewSet, basename="educationmiddle")
router.register(r'ape', ApeAPI, basename='ape')
router.register(r'courses', ApeAPI, basename='courses')
router.register(r'library', ApeAPI, basename='library')
router.register(r'education_pro', EducationProViewSet, basename='education_pro')
router.register(r'education_senior', EducationSeniorViewSet, basename='education_senior')
router.register(r'education_doctora', EducationDoctoraViewSet, basename='education_doctora')



urlpatterns = [
    path('welcomepage/int:pk/', WelcomePageObjectsViewSet.as_view({'get': 'retrieve'}), name="welcomepage"),
    path('educationmiddle/int:pk/', EducationMiddleObjectsViewSet.as_view({'get': 'retrieve'}), name="educationmiddle"),
    path('ape/int:pk/', ApeAPI.as_view({'get':'retrieve'}), name="ape"),
    path('courses/int:pk/', ApeAPI.as_view({'get':'retrieve'}), name="courses"),
    path('library/int:pk/', ApeAPI.as_view({'get':'retrieve'}), name="library"),  # replace with actual viewset for library objects
    path('welcomepageobjects/int:pk/', WelcomePageObjectsViewSet.as_view({'get':'retrieve'}), name="welcomepageobjects"),
    path('educationmiddleobjects/int:pk/', EducationMiddleObjectsViewSet.as_view({'get':'retrieve'}), name="educationmiddleobjects"),
]

urlpatterns += router.urls


