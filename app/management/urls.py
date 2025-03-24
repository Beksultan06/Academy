from django.urls import path
from app.management.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'name', NameAPI, basename='name')
router.register(r'rector', RectorViewSet, basename="rector")
router.register(r'scientworks-rector', ScientWorksRectorViewSet, basename="scientworks-rector")
router.register(r'hr-department', HR_departmentViewSet, basename="hr-department")
router.register(r'vacancies', VacanciesViewSet, basename="vacancies")
router.register(r'rector-objects-title', RectorObjectsTitleViewSet, basename="rector-objects-title")
router.register(r'vacancies-objects', VacanciesObjectsViewSet, basename="vacancies-objects")
router.register(r'hr-department-objects', HR_departmentObjectsViewSet, basename="hr-department-objects")
router.register(r'scientworks-rector-objects', ScientWorksRectorObjectsViewSet, basename="scientworks-rector-objects")

urlpatterns = [
    path('rector/<int:pk>/', RectorViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('scientworks-rector/<int:pk>/', ScientWorksRectorViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('hr-department/<int:pk>/', HR_departmentViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('vacancies/<int:pk>/', VacanciesViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('rector-objects-title/<int:pk>/', RectorObjectsTitleViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('vacancies-objects/<int:pk>/', VacanciesObjectsViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('hr-department-objects/<int:pk>/', HR_departmentObjectsViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('scientworks-rector-objects/<int:pk>/', ScientWorksRectorObjectsViewSet.as_view({'get': 'retrieve'}), name='news_detail'), 
    path('base', NameAPI.as_view, name='names'),
]

urlpatterns += router.urls