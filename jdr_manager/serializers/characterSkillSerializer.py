from rest_framework import serializers
from jdr_manager.models import CharacterSkill

class CharacterSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSkill
        fields = '__all__'


