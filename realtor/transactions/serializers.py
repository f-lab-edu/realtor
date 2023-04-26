from rest_framework import serializers

from .models import Agent, Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "mortgage_ratio", "down_payment", "start_date", "end_date", "agent"]


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ["id", "rating"]
