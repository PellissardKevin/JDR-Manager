from rest_framework import serializers
from jdr_manager.models import CharacterXP

class CharacterXPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterXP
        fields = '__all__'
