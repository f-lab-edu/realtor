# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse, Http404
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
from properties.models import Property
from rest_framework import generics
from properties.serializers import PropertySerializer


class PropertyList(generics.ListCreateAPIView):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        


