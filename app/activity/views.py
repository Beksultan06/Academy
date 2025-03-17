from django.shortcuts import render
from rest_framework import mixins
from app.activity.serializers import *
from app.activity.models import *
from rest_framework.viewsets import GenericViewSet


class ProgressViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class AllProgressViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = AllProgress.objects.all()
    serializer_class = AllProgressSerializer
    
class EducationalViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Educational.objects.all()
    serializer_class = EducationalSerializer