from rest_framework import viewsets
from jdr_manager.models import CharacterSkill
from jdr_manager.serializers import CharacterSkillSerializer

class CharacterSkillViewSet(viewsets.ModelViewSet):
    queryset = CharacterSkill.objects.all()
    serializer_class = CharacterSkillSerializer
