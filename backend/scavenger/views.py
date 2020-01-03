from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import ScavengerSerializer      
from .models import ScavengerHunt                 

class ScavengerView(viewsets.ModelViewSet):       
    serializer_class = ScavengerSerializer          
    queryset = ScavengerHunt.objects.all()              