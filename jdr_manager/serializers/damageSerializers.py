from rest_framework import serializers
from jdr_manager.models import Damage

class DamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damage
        fields = '__all__'
