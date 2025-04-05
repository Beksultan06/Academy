from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from app.mainpage.models import Settings
from app.mainpage.serializers import SettingsSerializers

class SettingsAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers