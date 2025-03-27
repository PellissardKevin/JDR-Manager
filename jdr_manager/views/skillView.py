from rest_framework import viewsets
from jdr_manager.models import Skill
from jdr_manager.serializers import SkillSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
