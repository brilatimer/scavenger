from django.contrib import admin
from django.urls import path, include                 
from rest_framework import routers                    
from scavenger import views 
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()                      
router.register(r'scavenger', views.ScavengerView, 'scavenger')     
router.register(r'clue', views.ClueView, 'clue')  
# router.register(r'register', views.RegistrationAPI, 'register')  

urlpatterns = [
    # path('',views.index),
    path('', login_required(views.FrontendAppView.as_view())),
    path('sms/', views.sms),
    path('admin/', admin.site.urls),   
    path('api/start_game/<int:scavenger_id>/', views.start_game),      
    path('api/', include(router.urls)),
    path('api/auth/', include('knox.urls')),
    path('api/auth/register/', views.RegistrationAPI.as_view()),   
    path('api/auth/loginnow/', views.LoginAPI.as_view()),
    path('auth/user/', views.UserAPI.as_view()),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('accounts/', include('django.contrib.auth.urls')),    # path(r'^', TemplateView.as_view(template_name="index.html")),
]        
