from django.shortcuts import render
from rest_framework import mixins
from app.management.serializers import *
from app.management.models import *
from rest_framework.viewsets import GenericViewSet

# Create your views here.
class NameAPI(GenericViewSet,
                mixins.ListModelMixin):
    queryset = Name.objects.all()
    serializer_class = NameSerializers

class RectorViewSet(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = Rector.objects.all()
    serializer_class = RectorSerializer

class ScientWorksRectorViewSet(GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    queryset = ScientWorksRector.objects.all()
    serializer_class = ScientWorksRectorSerializer
    
class HR_departmentViewSet(GenericViewSet,
                          mixins.ListModelMixin,
                        mixins.RetrieveModelMixin):
    queryset = HR_department.objects.all()
    serializer_class = HR_departmentSerializers
    
class VacanciesViewSet(GenericViewSet,
                       mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer

class RectorObjectsTitleViewSet(GenericViewSet,
                                mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = RectorObjectsTitle.objects.all()
    serializer_class = RectorObjectsTitleSerializer
    
class ScientWorksRectorObjectsViewSet(GenericViewSet,
                                     mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = ScientWorksRectorObjects.objects.all()
    serializer_class = ScientWorksRectorObjectsSerializer
    
class VacanciesObjectsViewSet(GenericViewSet,
                               mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = VacanciesObjects.objects.all()
    serializer_class = VacanciesObjectsSerializer
    
class HR_departmentObjectsViewSet(GenericViewSet,
                                  mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = HR_departmentObjects.objects.all()
    serializer_class = HR_departmentObjectsSerializer