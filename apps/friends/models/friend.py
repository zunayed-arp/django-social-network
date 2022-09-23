from django.db import models
from accounts.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Friend(models.Model):
    to_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="friends"
    )
    from_user = models.ForeignKey("User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("Friend")
        verbose_name_plural = _("Friends")

    def __str__(self) -> str:
        return f"User #{self.to_user_id} is friends with #{self.from_user_id}"

    def save(self, *args, **kwargs):
        print("friend model", kwargs)
        # Ensure users can't be friends with themselves
        if self.to_user.user == self.from_user.user:
            raise ValidationError("Users cannot be friends with themselves")
        super().save(*args, **kwargs)
