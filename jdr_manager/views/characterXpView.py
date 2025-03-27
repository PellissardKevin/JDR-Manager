from rest_framework import viewsets
from jdr_manager.models import CharacterXP
from jdr_manager.serializers import CharacterXPSerializer

class CharacterXPViewSet(viewsets.ModelViewSet):
    queryset = CharacterXP.objects.all()
    serializer_class = CharacterXPSerializer
