from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from apps.accounts.models import User
from apps.accounts.forms import UserRegistrationForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    success_url = "/"

    extra_context = {"title": "Register"}

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return HttpResponseRedirect(self.get_success_url())
    #     return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):
        email = request.POST["email"]
        if User.objects.filter(email=email).exists():
            messages.warning(request, "This email is already taken")
            return redirect("accounts:register")

        form_data = request.POST
        user_form = UserRegistrationForm(data=form_data)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            messages.success(request, "Successfully registered")
            return redirect("accounts:login")
        else:
            print(user_form.errors)
            return render(request, "accounts/register.html", {"form": user_form})
