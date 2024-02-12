from rest_framework import viewsets

from apps.player.models import Player
from apps.player.serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
