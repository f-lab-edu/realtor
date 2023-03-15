from django.shortcuts import render
from rest_framework import viewsets

from .models import ApplicationForm
from .models import Contract


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = ApplicationForm.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()