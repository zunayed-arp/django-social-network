from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User



class UserRegistrationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Enter username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Retype your password'})
        
    
    
    class Meta:
        model = User
        fields = ("username", "email", "gender", "password1", "password2")

        def clean_username(self):
            username = self.cleaned_data["username"]
            if " " in username:
                raise forms.ValidationError("User can't contain spaces.")
            return username

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.username = self.cleaned_data["username"]
            user.email = self.cleaned_data["email"]
            if commit == True:
                user.save()
            return user
