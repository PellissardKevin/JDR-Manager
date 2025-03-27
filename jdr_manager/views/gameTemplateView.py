from rest_framework import viewsets
from jdr_manager.models import GameTemplate
from jdr_manager.serializers import GameTemplateSerializer

class GameTemplateViewSet(viewsets.ModelViewSet):
    queryset = GameTemplate.objects.all()
    serializer_class = GameTemplateSerializer
