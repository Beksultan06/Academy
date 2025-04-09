from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet 
from .models import Photos
from .serializers import PhotosSerializer
# Create your views here.


class PhotosViewSet(GenericViewSet,
                    mixins.ListModelMixin):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['date']
    search_fields = ['date']
