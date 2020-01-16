from django.db import models
from django.contrib.auth.models import User

# Tutorial: add this
# class Todo(models.Model):
#   title = models.CharField(max_length=120)
#   description = models.TextField()
#   completed = models.BooleanField(default=False)
class Clue(models.Model):
  question = models.CharField(max_length=500)
  answer = models.CharField(max_length=500)
  hint = models.CharField(max_length=500)
  
  def __str__(self):
    return self.question
  
class ScavengerHunt(models.Model):
  # Who created the scavanager hunt
  # user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
  # Phone number of person playing the game
  # players_phone_number = models.CharField(max_length=100, blank=True)
  game_title = models.CharField(max_length=200)
  clues = models.ManyToManyField(Clue)
  owner = models.ForeignKey(User, related_name="scavenger_hunt",
          on_delete=models.CASCADE, null=True)

def __str__(self):
  return self.game_title

class Player(models.Model):
  players_phone_number = models.CharField(max_length=100, blank=True)
  scavenger_hunt = models.ForeignKey(ScavengerHunt,
              on_delete=models.CASCADE, null=True)
  which_clue = models.IntegerField(default = 0)
 