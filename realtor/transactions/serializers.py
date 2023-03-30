from rest_framework import serializers

from .models import Agent, Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "mortgage_ratio", "down_payment", "start_date", "end_date"]


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ["id", "username", "password", "email", "phone", "rating", "date_joined"]
