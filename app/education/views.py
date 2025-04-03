from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .models import AllEducation
from .serializers import AllEducationSerializer

class AllEducationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = AllEducation.objects.all()
    serializer_class = AllEducationSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})

        response = {
            "education": {
                "page": "Образование",
                "allEducation": serializer.data
            }
        }
        return Response(response)
