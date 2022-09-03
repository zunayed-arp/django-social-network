from ast import arg
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UsernameField
from apps.accounts.models import User


class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.user = None
        self.fields["email"].widget.attrs.update({"placeholder": "Enter Email"})
        self.fields["password"].widget.attrs.update({"placeholder": "Enter password"})

    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Password", strip=False, widget=forms.PasswordInput
    )

    def clean(self):
        email = self.cleaned_data.get["email"]
        password = self.cleaned_data.get["password"]

        if self.user == None:
            raise forms.ValidationError("User Does not Exists.")
        if not self.user.check_password(password):
            raise forms.ValidationError("Password does not match.")
        if not self.user.is_active:
            raise forms.ValidationError("user is not active.")
        return self.cleaned_data
        # return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user
