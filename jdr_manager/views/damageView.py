from rest_framework import viewsets
from jdr_manager.models import Damage
from jdr_manager.serializers.damageSerializers import DamageSerializer

class DamageViewSet(viewsets.ModelViewSet):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
