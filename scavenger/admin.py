from django.contrib import admin
from .models import ScavengerHunt, Clue


class ScavengerAdmin(admin.ModelAdmin):
  list_display = ('players_phone_number', 'game_title') 

admin.site.register(ScavengerHunt, ScavengerAdmin) 

class ClueAdmin(admin.ModelAdmin):
  list_display = ('question', 'answer', 'hint') 

admin.site.register(Clue, ClueAdmin) 