from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from ..models import Profile

class ProfileEditView(UpdateView):

    model = Profile
    template_name="profile/edit_profile.html"
    context_object_name="profile"
    object=None
    fields="__all__"
    
    def get_object(self,queryset=None):
        return self.request.user.profile
    
    def post(self,request,*args,**kwargs):
        print(request.data)
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.about = request.POST.get('about')
        if request.POST.get('gender')=="male":
            user.gender = "male"
        else:
            user.gender="female"
        user.save()
        
        profile = user.profile
        profile.country = request.POST.get('country')
        profile.city=request.POST.get('city')
        profile.phone = request.POST.get('phone')
        profile.save()
        return redirect(reverse_lazy('profile:edit_profile'))
        