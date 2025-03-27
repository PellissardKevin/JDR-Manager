from rest_framework import viewsets
from jdr_manager.models import Spell
from jdr_manager.serializers import SpellSerializer

class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
