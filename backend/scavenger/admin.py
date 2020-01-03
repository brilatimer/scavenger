from django.contrib import admin
from .models import ScavengerHunt

class ScavengerAdmin(admin.ModelAdmin):
  list_display = ('players_phone_number', 'game_title') 

admin.site.register(ScavengerHunt, ScavengerAdmin) 