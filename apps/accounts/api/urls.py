import imp
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
# from .custom_claims import MyTokenObtainPairView
from .views import LogoutAPIView, RegistrationAPIView,MyTokenObtainPairView
urlpatterns =[
    path("register/",RegistrationAPIView.as_view()),
    path("login/",MyTokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("logout/",LogoutAPIView.as_view()),
   
    
]