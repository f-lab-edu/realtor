from django.shortcuts import render
from rest_framework import viewsets

from .models import Property


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()

    



