from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.students.models import *
from app.students.serializers import *



class NameAPI(GenericViewSet,
                mixins.ListModelMixin):
    queryset = Name.objects.all()
    serializer_class = NameSerializers
    

class ParliamentAPI(GenericViewSet, 
                    mixins.ListModelMixin,):
    queryset = Parliament.objects.all()
    serializer_class = ParliamentSerializer

class ActiveAPI(GenericViewSet, 
                mixins.ListModelMixin,):
    queryset = Active_Students.objects.all()
    serializer_class = ActiveSerializer

class Active_StudentsAboutApi(GenericViewSet,
                                mixins.ListModelMixin,):
        queryset = Active_StudentsAbout.objects.all()
        serializer_class = Active_StudentsAboutSerializer

class HostelAPI(GenericViewSet, 
                mixins.ListModelMixin,):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class PortalAPI(GenericViewSet,
                mixins.ListModelMixin,):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer 

class StudentLifeAPI(GenericViewSet, 
                     mixins.ListModelMixin,):
    queryset = StudentsLife.objects.all()
    serializer_class = StudentsLifeSerializer

class ListPagesAPI(GenericViewSet,
                   mixins.ListModelMixin):
    queryset = ListPages.objects.all()
    serializer_class = ListPagesSerializer
