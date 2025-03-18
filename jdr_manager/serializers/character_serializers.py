from rest_framework import serializers
from jdr_manager.models import CharacterSheet, CharacterXP, Damage, Skill, Spell
from .user_serializers import CustomUserSerializer
from .damage_serializers import DamageSerializer
from .skill_serializers import SkillSerializer
from .spell_serializers import SpellSerializer

class CharacterSheetSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)  # Affichage détaillé des compétences
    spells = SpellSerializer(many=True, read_only=True)  # Affichage détaillé des sorts
    injuries = DamageSerializer(many=True, read_only=True)  # Affichage détaillé des blessures

    class Meta:
        model = CharacterSheet
        fields = '__all__'

class CharacterXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterXP
        fields = '__all__'
