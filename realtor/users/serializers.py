from rest_framework import serializers

from .models import Agent, Application, Contract, PreferredProperty, User


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


class AgentSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Agent
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Application
        fields = ["id", "status", "comment", "user", "agent", "created_at", "updated_at"]


class PreferredPropertySerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

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
            "user",
        ]


class ContractSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    agent = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Contract
        fields = "__all__"
