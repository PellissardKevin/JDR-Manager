from rest_framework import serializers
from .itemSerializer import ItemSerializer
from jdr_manager.models import CharacterInventory

# Serializer pour l'inventaire du personnage
class CharacterInventorySerializer(serializers.ModelSerializer):
    item = ItemSerializer()  # Sérialisation complète de l'objet

    class Meta:
        model = CharacterInventory
        fields = ['id', 'character', 'item', 'quantity']
