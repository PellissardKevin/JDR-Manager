from rest_framework import viewsets
from jdr_manager.models import Item
from jdr_manager.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
