from rest_framework import serializers

from ...models import User


# class UserSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         kwargs["partial"] = True
#         super(UserSerializer, self).__init__(*args, **kwargs)

#     class Meta:
#         model = User
#         exclude = (
#             "password",
#             "user_permissions",
#             "groups",
#         )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        label="confirm password",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if username and User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "username must be unique"})
        if email and User.objects.filter(email=email, username=username).exists():
            raise serializers.ValidationError({"email": "Email  must be unique"})
        if password != password2:
            raise serializers.ValidationError({"password": "passwords does not match"})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
