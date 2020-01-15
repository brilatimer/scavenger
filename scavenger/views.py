from django.shortcuts import render, redirect 
from rest_framework import viewsets          
from .serializers import ScavengerSerializer, ClueSerializer
from .models import ScavengerHunt, Clue    
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer
from django.contrib.auth.decorators import login_required 
from django.conf import settings

# @login_required
# def index(request):
#     # if settings.ENVIRONMENT == 'local':
#     return redirect("http://localhost:3000") 
#     # else:
#     #     return redirect("http://localhost:3000")

from django.views.generic import View
from django.http import HttpResponse
import os

from twilio import twiml

from django.http import JsonResponse


def sms(request):
    # print(request)
    # (twilio_number, twilio_account_sid, twilio_auth_token) = settings.load_twilio_config()
    # resp = twiml.Response()

    # # Add a message
    # resp.message("The Robots are coming! Head for the hills!")

    return JsonResponse(request.POST)

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        if settings.ENVIRONMENT == 'local':
            return redirect("http://localhost:3000") 
        
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return redirect("http://localhost:3000") 
            # return HttpResponse(
            #     """
            #     This URL is only used when you have built the production
            #     version of the app. Visit http://localhost:3000/ instead, or
            #     run `yarn run build` to test the production version.
            #     """,
            #     status=501,
            # )
            
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