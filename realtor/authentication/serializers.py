from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def validate_username(self, validated_data):

        if len(validated_data) < 3:
            raise serializers.ValidationError("username is too short!")

        if User.objects.filter(username=validated_data).exists():
            raise serializers.ValidationError("username is already taken!")
        else:
            return validated_data

    def validate_password(self, validated_date):
        password_validation.validate_password(validated_date)
        return validated_date

    def get_and_authenticate_user(username, password):
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username or password. Please try again!")
        return user

    def create(self, validated_data):

        username = validated_data["username"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        return user


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    last_login = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if username is None:
            raise serializers.ValidationError("an username address is required to log in.")
        if password is None:
            raise serializers.ValidationError("a password is required to log in")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("A user with this username and password was not found")
        if not user.is_active:
            raise serializers.ValidationError("this user has been deactivated")

        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])

        return {"email": user.email, "username": user.username, "last_login": user.last_login}
