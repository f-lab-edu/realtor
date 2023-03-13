from django.db import models
from properties.enums import PropertyType, DetailedType, StatusType


class Property(models.Model):

    image = models.CharField(max_length=50)
    price = models.IntegerField()
    # address = models.CharField(max_length=30)
    city = models.CharField(max_length=5)
    district = models.CharField(max_length=3)
    zone = models.CharField(max_length=3)
    property_type = models.IntegerField(choices = PropertyType.choices)
    detailed_type = models.IntegerField(choices = DetailedType.choices)
    size = models.IntegerField()
    description = models.TextField()
    maintenance_cost = models.IntegerField()
    status = models.IntegerField(choices = StatusType.choices) 


class PreferredProperty(models.Model):
    
    city = models.CharField(max_length=5)
    district = models.CharField(max_length=3)
    zone = models.CharField(max_length=3)
    property_type = models.IntegerField(choices = PropertyType.choices)
    detailed_type = models.IntegerField(choices = DetailedType.choices)
    budget_from = models.IntegerField()
    budget_to = models.IntegerField()
    description = models.TextField()
    


