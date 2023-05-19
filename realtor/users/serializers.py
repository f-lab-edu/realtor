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
    class Meta:
        model = Agent
        fields = ["id", "rating"]


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


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "mortgage_ratio", "down_payment", "start_date", "end_date", "agent"]
