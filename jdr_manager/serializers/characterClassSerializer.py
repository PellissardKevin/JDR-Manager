from rest_framework import serializers
from jdr_manager.models import CharacterClass

class CharacterClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterClass
        fields = '__all__'
