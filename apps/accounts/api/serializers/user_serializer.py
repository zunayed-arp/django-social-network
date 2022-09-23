from rest_framework import serializers

from ...models import User


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs["partial"] = True
        super(UserSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        exclude = (
            "password",
            "user_permissions",
            "groups",
        )
