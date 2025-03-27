from rest_framework import serializers
from jdr_manager.models import GameTemplate

class GameTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTemplate
        fields = '__all__'
