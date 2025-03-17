from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import AcademicCouncil, ScientificJournals, CenterEducation
from .serializers import AcademicCouncilSerializer, ScientificJournalsSerializer, CenterEducationSerializer

class AcademicCouncilAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = AcademicCouncil.objects.all()
    serializer_class = AcademicCouncilSerializer

class ScientificJournalsAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = ScientificJournals.objects.all()
    serializer_class = ScientificJournalsSerializer

class CenterEducationAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = CenterEducation.objects.all()
    serializer_class = CenterEducationSerializer
