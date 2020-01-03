from rest_framework import serializers
from .models import ScavengerHunt, Clue

class ClueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clue
    fields = ('id','question', 'answer', 'hint')

class ScavengerSerializer(serializers.ModelSerializer):
  clues = ClueSerializer(many=True)
  
  class Meta:
    model = ScavengerHunt
    fields = ('id','players_phone_number', 'game_title', 'clues')
    
def create(self, validated_data):
    clues_data = validated_data.pop('clues')
    scavenger_hunt = ScavengerHunt.objects.create(**validated_data)
    for clue_data in clues_data:
        clue.objects.create(scavenge=scavenger_hunt, **clue_data)
    return scavenger_hunt