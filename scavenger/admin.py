from django.contrib import admin
from .models import ScavengerHunt, Clue, Player

class ScavengerAdmin(admin.ModelAdmin):
  list_display = ('game_title',) 

admin.site.register(ScavengerHunt, ScavengerAdmin) 

class ClueAdmin(admin.ModelAdmin):
  list_display = ('question', 'answer', 'hint') 

admin.site.register(Clue, ClueAdmin) 

class PlayerAdmin(admin.ModelAdmin):
  list_display = ('players_phone_number', 'scavenger_hunt', 'which_clue') 

admin.site.register(Player, PlayerAdmin) 