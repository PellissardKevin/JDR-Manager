from rest_framework import viewsets
from jdr_manager.models import CharacterClass
from jdr_manager.serializers import CharacterClassSerializer

class CharacterClassViewSet(viewsets.ModelViewSet):
    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer
