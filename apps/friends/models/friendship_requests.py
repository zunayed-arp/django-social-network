from django.db import models


class FriendshipRequest(models.Model):
    """Model to represent friendship requests"""

    from_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="friendship_request_sent"
    )

    to_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="friendship_requests_received"
    )
