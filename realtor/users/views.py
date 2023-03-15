from django.shortcuts import render
from rest_framework import viewsets

from .models import User
from .models import Agent


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
