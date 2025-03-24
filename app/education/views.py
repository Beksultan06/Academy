from django.shortcuts import render
from app.education.models import *
from app.education.serializers import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Create your views here.

class NameAPI(GenericViewSet,
                mixins.ListModelMixin):
    queryset = Name.objects.all()
    serializer_class = NameSerializers
    
class WelcomePageViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = WelcomePage.objects.all()
    serializer_class = WelcomePageSerializer

class EducationMiddleViewSet(GenericViewSet,
                            mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = EducationMiddle.objects.all()
    serializer_class = EducationMiddleSerializer

class ApeAPI(GenericViewSet,
             mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = Ape.objects.all()
    serializer_class = ApeSerializer

class CoursesAPI(GenericViewSet,
                 mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class LibraryAPI(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    
class EducationProViewSet(GenericViewSet,
                            mixins.ListModelMixin):
    queryset = EducationPro.objects.all()
    serializer_class = EducationProSerializer


class EducationSeniorViewSet(GenericViewSet,
                            mixins.ListModelMixin):
    queryset = EducationSenior.objects.all()
    serializer_class = EducationSeniorSerializer


class EducationDoctoraViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = EducationDoctora.objects.all()
    serializer_class = EducationDoctoraSerializer
    
class WelcomePageObjectsViewSet(GenericViewSet,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin):
    queryset = WelcomePageObjects.objects.all()
    serializer_class = WelcomePageObjectsSerializer
    
class EducationMiddleObjectsViewSet(GenericViewSet,
                                    mixins.ListModelMixin,
                                    mixins.RetrieveModelMixin):
    queryset = EducationMiddleObjects.objects.all()
    serializer_class = EducationMiddleObjectSerializer
    
    
class EducationDoctoraObjectsViewSet(GenericViewSet,
                                     mixins.ListModelMixin,
                                     mixins.RetrieveModelMixin):
    queryset = EducationDoctoraObjects.objects.all()
    serializer_class = EducationDoctoraObjectsSerializer
    
class EducationProObjectsViewSet(GenericViewSet,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin):
    queryset = EducationProObjects.objects.all()
    serializer_class = EducationProObjectsSerializer
    

class EducationSeniorObjectsViewSet(GenericViewSet,
                                     mixins.ListModelMixin,
                                     mixins.RetrieveModelMixin):
    queryset = EducationSeniorObjects.objects.all()
    serializer_class = EducationSeniorObjectsSerializer
    