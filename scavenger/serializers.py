from rest_framework import serializers
from .models import ScavengerHunt, Clue
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ClueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clue
    fields = ('id','question', 'answer', 'hint')
    
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

class ScavengerSerializer(serializers.ModelSerializer):
  clues = ClueSerializer(many=True)
  
  class Meta:
    model = ScavengerHunt
    fields = ('id', 'game_title', 'clues')
      
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
      # instance.players_phone_number = validated_data.get('players_phone_number', instance.players_phone_number)
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
  