from django.db import models

# Tutorial: add this
# class Todo(models.Model):
#   title = models.CharField(max_length=120)
#   description = models.TextField()
#   completed = models.BooleanField(default=False)

class ScavengerHunt(models.Model):
  # Who created the scavanager hunt
  # user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
  # Phone number of person playing the game
  players_phone_number = models.CharField(max_length=100)
  game_title = models.CharField(max_length=200)
  # game_info = JSONField()


def _str_(self):
  return self.title