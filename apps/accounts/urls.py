from django.urls import path,include
from .views import TimelineView,ProfileEditView

app_name = "accounts"

urlpatterns = [
   path('edit-profile/',ProfileEditView.as_view(),name="edit-profile"),
   path('<slug:username>/',TimelineView.as_view(),name="user-timeline"),
]