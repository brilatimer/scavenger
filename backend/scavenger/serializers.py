from rest_framework import serializers
from .models import ScavengerHunt

class ScavengerSerializer(serializers.ModelSerializer):
  class Meta:
    model = ScavengerHunt
    fields = ('players_phone_number', 'game_title')