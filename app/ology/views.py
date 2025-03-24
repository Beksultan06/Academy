from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import *
from .serializers import *



class ScientificJournalsObjectAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = ScientificJournalsObject.objects.all()
    serializer_class = ScientificJournalsObjectSerializer


class NameAPI(GenericViewSet,
                mixins.ListModelMixin):
    queryset = Name.objects.all()
    serializer_class = NameSerializers
    

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
