from django.urls import path,include

from apps.accounts.views import *

app_name = "accounts"

urlpatterns = [
   path('register',RegisterView.as_view(),name='register'),
   path('login',LoginView.as_view(),name='login'),
   
]