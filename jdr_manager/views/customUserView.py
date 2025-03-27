from rest_framework import viewsets
from jdr_manager.models import CustomUser
from jdr_manager.serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
