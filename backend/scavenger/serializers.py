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
          clue = Clue.objects.create()
          scavenger_hunt.clues.add(clue)
          clue.question = clue_data.get('question', '')
          clue.answer = clue_data.get('answer', '')
          clue.hint = clue_data.get('hint', '')
          clue.save()
      return scavenger_hunt
    
  def update(self, instance, validated_data):
      # import pdb; pdb.set_trace()
      clues_data = validated_data.pop('clues')
      clues = (instance.clues).all()
      clues = list(clues)
      instance.players_phone_number = validated_data.get('players_phone_number', instance.players_phone_number)
      instance.game_title = validated_data.get('game_title', instance.game_title)
      instance.save()

      for clue_data in clues_data:
          clue = None
          if len(clues) > 0:
            clue = clues.pop(0)
          else:
            clue = Clue.objects.create()
            instance.clues.add(clue)
          clue.question = clue_data.get('question', '')
          clue.answer = clue_data.get('answer', '')
          clue.hint = clue_data.get('hint', '')
          clue.save()
      return instance
  