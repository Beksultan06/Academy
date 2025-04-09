from rest_framework.views import APIView
from rest_framework.response import Response
from app.AboutAcademy.models import About
from app.AboutAcademy.serializers import AboutSerializer
from collections import defaultdict

class AboutGroupedView(APIView):
    def get(self, request):
        about_pages = About.objects.prefetch_related('images').all()
        grouped = defaultdict(list)

        for about in about_pages:
            serializer = AboutSerializer(about, context={'request': request})
            grouped[about.page_key].append(serializer.data)

        return Response(grouped)