from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):

    """Define a model manager for User model with username and email field"""

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise (_("You must provide a valid email address"))

    def _create_user(self, username, email, password, **extra_fields):
        """Create and save a User with the given username,email and password."""
        if not username:
            raise ValueError(_("User must submit a username."))
        if not email:
            raise ValueError(_("User must submit an email."))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base user account: an email address is required."))

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self,username,email,password,**extra_fields):
        """Create and save a regular User with the given username,email and password."""
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        extra_fields.setdefault("status",False)
        return self._create_user(username,email,password,**extra_fields)
    
    def create_superuser(self,username,email,password,**extra_fields):
         """Create and save a superuser with the given username,email and password."""
         extra_fields.setdefault("is_staff",True)
         extra_fields.setdefault("is_superuser",True)
         extra_fields.setdefault("status",False)
         
         if extra_fields.get("is_staff") is not True:
             raise ValueError(_("superuser must have is_staff=True"))
         if extra_fields.get("is_superuser") is not True:
             raise ValueError(_("superuser must have is_superuser=True"))
         
         return self._create_user(username,email,password,**extra_fields)
        
