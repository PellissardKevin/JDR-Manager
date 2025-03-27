from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from jdr_manager.models import CharacterSheet, CustomUser
from jdr_manager.serializers import CharacterSheetSerializer

class CharacterSheetViewSet(viewsets.ModelViewSet):
    queryset = CharacterSheet.objects.all()
    serializer_class = CharacterSheetSerializer
