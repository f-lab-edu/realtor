from rest_framework import serializers
from .models import Property, PreferredProperty
from properties.enums import PropertyType, DetailedType, StatusType


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'image', 'price', 'city', 'district', 'zone', 'property_type',
                  'detailed_type', 'size', 'description', 'maintenance_cost', 'status']
