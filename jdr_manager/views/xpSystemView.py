from rest_framework import viewsets
from jdr_manager.models import XpSystem
from jdr_manager.serializers import XpSystemSerializer

class XpSystemViewSet(viewsets.ModelViewSet):
    queryset = XpSystem.objects.all()
    serializer_class = XpSystemSerializer
