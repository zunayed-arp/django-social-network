from django.contrib.auth.models import AbstractUser
from django.db import models

from ..managers import UserManager


class User(AbstractUser):
    username = models.CharField(
        "username",
        max_length=50,
        unique=True,
        help_text="Required. 50 characters or fewer. Letters, digits and @/./+/-/_only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        error_messages={"unique": "A user with that email already exists."},
    )

    gender = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
