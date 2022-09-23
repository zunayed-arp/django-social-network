from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, UpdateView

from apps.accounts.models import User, Profile


class TimelineView(DetailView):
    model = User
    template_name = "accounts/user_profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"
    object = None
    
    def get_object(self,queryset=None):
        # return self.model.objects.select_related('profile').prefetch_related('posts').get(username=self.kwargs.get(self.slug_url_kwarg))
        data = self.model.objects.select_related('profile')
        # print(data)
        return data
    
    def get(self,request,*args,**kwargs):
        print(kwargs.get('username'))
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
