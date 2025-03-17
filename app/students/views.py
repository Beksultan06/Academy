from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.students.models import *
from app.students.serializers import *

class ParliamentAPI(GenericViewSet, 
                    mixins.ListModelMixin,):
    queryset = Parliament.objects.all()
    serializer_class = ParliamentSerializer

class ActiveAPI(GenericViewSet, 
                mixins.ListModelMixin,):
    queryset = Active.objects.all()
    serializer_class = ActiveSerializer


class HostelAPI(GenericViewSet, 
                mixins.ListModelMixin,):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class StudentLifeAPI(GenericViewSet, 
                     mixins.ListModelMixin,):
    queryset = StudentLife.objects.all()
    serializer_class = StudentLifeSerializer

