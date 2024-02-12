from rest_framework import serializers

from apps.player.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'firstname', 'lastname', )
