
from django.contrib.auth import get_user_model
from rest_framework import permissions,status,response
from rest_framework.views import APIView
from ..serializers import UserSerializer,UserCreateSerializer
from django.contrib.auth import logout
    
class LogoutAPIView(APIView):
    def get(self,request):
        logout(request)
        return response.Response({"message":"Loggedout Successfully"})
        
        