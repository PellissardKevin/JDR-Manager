from rest_framework import serializers
from jdr_manager.models import XpSystem

class XpSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = XpSystem
        fields = '__all__'
