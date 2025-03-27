from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from jdr_manager.models import Campaign, CustomUser
from jdr_manager.serializers import CampaignSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    # Action personnalisée pour ajouter un joueur a la campagne
    @action(detail=True, methods=['post'])
    def add_player(self, request, pk=None):
        campaign = self.get_object()
        user_id = request.data.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        campaign.players.add(user)
        campaign.save()
        return Response({'status': 'player added'})

    # Action personnalisée pour "activer" ou "désactiver" une campagne
    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        campaign = self.get_object()
        campaign.is_active = not campaign.is_active
        campaign.save()
        return Response({"status": "success", "is_active": campaign.is_active})
