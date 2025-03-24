from rest_framework import serializers
from jdr_manager.models import Item

# Serializer pour les objets
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
