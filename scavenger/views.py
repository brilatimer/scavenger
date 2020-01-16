from django.shortcuts import render, redirect 
from rest_framework import viewsets          
from .serializers import ScavengerSerializer, ClueSerializer
from .models import ScavengerHunt, Clue, Player   
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer
from django.contrib.auth.decorators import login_required 
from django.conf import settings
import json
from twilio.rest import Client

# @login_required
# def index(request):
#     # if settings.ENVIRONMENT == 'local':
#     return redirect("http://localhost:3000") 
#     # else:
#     #     return redirect("http://localhost:3000")

from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden
import os

from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from functools import wraps
from twilio.request_validator import RequestValidator


def validate_twilio_request(f):
    """Validates that incoming requests genuinely originated from Twilio"""
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        # Create an instance of the RequestValidator class
        validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)

        # Validate the request using its URL, POST data,
        # and X-TWILIO-SIGNATURE header
        request_valid = validator.validate(
            request.build_absolute_uri(),
            request.POST,
            request.META.get('HTTP_X_TWILIO_SIGNATURE', ''))

        # Continue processing the request if it's valid, return a 403 error if
        # it's not
        if request_valid:
            return f(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated_function

@validate_twilio_request
@require_POST
@csrf_exempt
def sms(request):
    """Twilio Messaging URL - receives incoming messages from Twilio"""
    # Create a new TwiML response
    resp = MessagingResponse()
    
    
    text_body = request.POST['Body'].lower() # contents of the sms, but lower case
    phone_number = request.POST['From']
    if text_body == "hint":
        resp.message(phone_number)
        return HttpResponse(resp)


    # <Message> a text back to the person who texted us
    body = "Your text to me was {0} characters long. Webhooks are neat :)" \
        .format(len(text_body))
    resp.message(body)

    # Return the TwiML
    return HttpResponse(resp)

@csrf_exempt
def start_game(request, scavenger_id):
    scavenger = ScavengerHunt.objects.get(pk=scavenger_id)
    content = json.loads(request.body)
    phone_number = content['players_phone_number']

    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
    .create(
        body=scavenger.clues.all()[0], # always send the first clue
        from_=settings.TWILIO_NUMBER,
        to=phone_number
    )
    Player.objects.create(players_phone_number= phone_number, scavenger_hunt= scavenger, which_clue= 0)

    return HttpResponse()

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