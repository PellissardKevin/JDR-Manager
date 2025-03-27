from rest_framework import viewsets
from jdr_manager.models import CharacterInventory
from jdr_manager.serializers import CharacterInventorySerializer

class CharacterInventoryViewSet(viewsets.ModelViewSet):
    queryset = CharacterInventory.objects.all()
    serializer_class = CharacterInventorySerializer
