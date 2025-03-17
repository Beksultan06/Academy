from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import *
from .serializers import *

class AcademicAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer

class Admissions_CommitteeAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = Admissions_Committee.objects.all()
    serializer_class = Admissions_CommitteeSerializer
