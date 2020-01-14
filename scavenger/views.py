from django.shortcuts import render, redirect 
from rest_framework import viewsets          
from .serializers import ScavengerSerializer, ClueSerializer
from .models import ScavengerHunt, Clue    
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer
from django.contrib.auth.decorators import login_required 

@login_required
def index(request):
    return redirect("http://localhost:3000") 
          
class ScavengerView(viewsets.ModelViewSet):       
    serializer_class = ScavengerSerializer          
    queryset = ScavengerHunt.objects.all()              
    
class ClueView(viewsets.ModelViewSet):       
    serializer_class = ClueSerializer          
    queryset = Clue.objects.all()  

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })    

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })    

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user   
    
class ScavengerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ScavengerSerializer

    def get_queryset(self):
        return self.request.user.scavengers.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 