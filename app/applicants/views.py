from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from . models import Academic
from . serializers import AcademicSerializer

class AcademicViewSet(ViewSet):
    def list(self, request):
        academics = Academic.objects.all()
        serializer = AcademicSerializer(academics, many=True, context={'request': request})

        response = {
            "academics": {
                "page": "Абитуриентам",
                "banner": {
                    "title": "Поступить в академию",
                    "description": "Информация для абитуриентов о поступлении, контактах и деталях обучения."
                },
                "data": serializer.data
            }
        }
        return Response(response)
