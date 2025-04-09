from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.ology.models import Ology
from app.ology.serializers import OlogySerializer
from collections import defaultdict

class OlogyViewSet(ViewSet):
    def list(self, request):
        societies = Ology.objects.all()
        grouped = defaultdict(list)

        for society in societies:
            serializer = OlogySerializer(society, context={'request': request})
            grouped[society.link].append(serializer.data)

        nav_elements = []
        for i, (link, cards) in enumerate(grouped.items(), start=1):
            nav_elements.append({
                "id": i,
                "link": link,
                "cards": cards
            })

        response = {
            "societies": {
                "page": "Общества",
                "banner": {
                    "title": "Наши Общества",
                    "description": "Разнообразие обществ, в которых студенты могут развиваться и расти."
                },
                "navElements": nav_elements
            }
        }
        return Response(response)
