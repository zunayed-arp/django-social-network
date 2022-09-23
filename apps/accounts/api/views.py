
from django.contrib.auth import get_user_model
from rest_framework import permissions,status,response
from rest_framework.views import APIView
from .serializers import UserSerializer,UserCreateSerializer
from django.contrib.auth import logout

class RegistrationAPIView(APIView):
    def post(self,request):
        data  = request.data
        serializer = UserCreateSerializer(data=data)
        if not serializer.is_valid(raise_exception=True):
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        res = {
            "status":True,
            "message":"Successfully Registered"
        }
        return response.Response(res,status=status.HTTP_201_CREATED)
    
class LogoutAPIView(APIView):
    def get(self,request):
        logout(request)
        return response.Response({"message":"Loggedout Successfully"})
        
        