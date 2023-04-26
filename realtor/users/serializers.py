from rest_framework import serializers

from .models import Application, PreferredProperty, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "date_joined",
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "status", "comment", "agent", "user", "created_at", "updated_at"]


class PreferredPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferredProperty
        fields = [
            "id",
            "city",
            "district",
            "zone",
            "property_type",
            "detailed_type",
            "budget_from",
            "budget_to",
            "description",
        ]
