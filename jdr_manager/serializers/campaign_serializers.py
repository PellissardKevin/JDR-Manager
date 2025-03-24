from rest_framework import serializers
from jdr_manager.models import Campaign, XpSystem
from .user_serializers import CustomUserSerializer  # Pour afficher les détails du MJ


class CampaignSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer(read_only=True)  # Afficher le MJ en détail

    class Meta:
        model = Campaign
        fields = '__all__'

