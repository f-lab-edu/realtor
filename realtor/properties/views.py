from django.shortcuts import render
from rest_framework import viewsets

from .models import Property, PreferredProperty


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()


class PreferredPropertyViewSet(viewsets.ModelViewSet):
    queryset = PreferredProperty.objects.all()



