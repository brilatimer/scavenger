from django.contrib import admin
from django.urls import path, include                 
from rest_framework import routers                    
from scavenger import views 

router = routers.DefaultRouter()                      
router.register(r'scavenger', views.ScavengerView, 'scavenger')     
router.register(r'clue', views.ClueView, 'clue')  
# router.register(r'register', views.RegistrationAPI, 'register')  

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('api/', include(router.urls)),
    path('api/auth/', include('knox.urls')),
    path('api/auth/register/', views.RegistrationAPI.as_view()),   
    path('api/auth/loginnow/', views.LoginAPI.as_view()),
    path('auth/user/', views.UserAPI.as_view()),
    # path(r'^', TemplateView.as_view(template_name="index.html")),
]        
