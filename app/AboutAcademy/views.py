from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import About
from .serializers import AboutSerializer

class AboutViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            about = About.objects.prefetch_related('images').get(page_key=pk)
        except About.DoesNotExist:
            return Response({"detail": "Страница не найдена"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, context={'request': request})
        return Response(serializer.data)