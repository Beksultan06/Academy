from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.students.views import *

router = DefaultRouter()

router.register(r'name', NameAPI, basename='name')
router.register('parliament', ParliamentAPI, basename='parliament')
router.register('active', ActiveAPI, basename='active')
router.register('hostel', HostelAPI, basename='hostel')
router.register('portal', PortalAPI, basename='portal')
router.register('studentlife', StudentLifeAPI, basename='studentlife')
router.register('listpages', ListPagesAPI, basename='listpages')    


urlpatterns = [
    path('', include(router.urls)), 
]
