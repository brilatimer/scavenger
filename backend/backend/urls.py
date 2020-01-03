from django.contrib import admin
from django.urls import path, include                 
from rest_framework import routers                    
from scavenger import views                            

router = routers.DefaultRouter()                      
router.register(r'scavenger', views.ScavengerView, 'scavenger')     
router.register(r'clue', views.ClueView, 'clue')     


urlpatterns = [
    path('admin/', admin.site.urls),         path('api/', include(router.urls))                # add this
    ]