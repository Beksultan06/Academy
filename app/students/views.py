from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import *
from .models import *
from collections import defaultdict
from rest_framework.viewsets import GenericViewSet


class ScientificJournalViewSet(ViewSet):
    def list(self, request):
        journals = ScientificJournal.objects.all()
        grouped = defaultdict(list)

        for journal in journals:
            serializer = ScientificJournalSerializer(journal, context={'request': request})
            grouped[journal.title].append(serializer.data)

        nav_elements = []
        for i, (link, cards) in enumerate(grouped.items(), start=1):
            nav_elements.append({
                "id": i,
                "cards": cards
            })


        return Response({"nav_elements": nav_elements})