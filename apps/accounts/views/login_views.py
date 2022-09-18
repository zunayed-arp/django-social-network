from ast import arg
from django.contrib import messages,auth
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import FormView
from apps.accounts.forms import UserLoginForm


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = "accounts/login.html"
    success_url="/"
    
    extra_context={
        'title':'Login'
    }
    
    # def dispatch(self,request,*args,**kwargs):
    #     if self.request.user.is_authenticated:
    #         return HttpResponseRedirect(self.get_success_url())
    #     return super().dispatch(self.request,*args,**kwargs)
    
    def get_form_class(self):
        return self.form_class
    
    def form_valid(self,form):
        auth.login(self.request,form.get_user())
        on_success = self.get_success_url()
        return HttpResponseRedirect(on_success)
    
    def form_invalid(self, form):
        context_data = self.get_context_data(form=form)
        return self.render_to_response(context_data)