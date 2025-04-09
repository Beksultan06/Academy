from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from app.mainpage.models import Settings, NewsMain, Magazine
from app.mainpage.serializers import SettingsSerializers, NewsMainSerializer, MagazineSerializer

class SettingsAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers

class NewsMainViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsMain.objects.prefetch_related('cards')
    serializer_class = NewsMainSerializer


class MagazineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Magazine.objects.prefetch_related('cards')
    serializer_class = MagazineSerializer