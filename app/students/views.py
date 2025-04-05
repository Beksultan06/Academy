from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import *
from .models import *
from collections import defaultdict
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class ScientificJournalViewSet(ViewSet):
    def list(self, request):
        journals = ScientificJournal.objects.all()
        grouped = defaultdict(list)

        for journal in journals:
            serializer = ScientificJournalSerializer(journal, context={'request': request})
            grouped[journal.link].append(serializer.data)

        nav_elements = []
        for i, (link, cards) in enumerate(grouped.items(), start=1):
            nav_elements.append({
                "id": i,
                "link": link,
                "cards": cards
            })

        response = {
            "scientific_journal": {
                "page": "Научные журналы",
                "banner": {
                    "title": "Наши Научные Журналы",
                    "description": "Публикуем лучшие работы студентов и преподавателей."
                },
                "navElements": nav_elements
            }
        }
        return Response(response)


