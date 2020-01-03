from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import ScavengerSerializer, ClueSerializer
from .models import ScavengerHunt, Clue              

class ScavengerView(viewsets.ModelViewSet):       
    serializer_class = ScavengerSerializer          
    queryset = ScavengerHunt.objects.all()              
    
class ClueView(viewsets.ModelViewSet):       
    serializer_class = ClueSerializer          
    queryset = Clue.objects.all()              