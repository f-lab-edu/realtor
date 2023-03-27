from django.db import models
from properties.enums import DetailedType, PropertyType, StatusType


class Property(models.Model):

    image = models.CharField(max_length=50, blank=True, default="")
    price = models.IntegerField()
    city = models.CharField(max_length=5)
    district = models.CharField(max_length=3)
    zone = models.CharField(max_length=3)
    property_type = models.IntegerField(
        choices=PropertyType.choices, default=PropertyType.PURCHASE
    )
    detailed_type = models.IntegerField(
        choices=DetailedType.choices, default=DetailedType.APARTMENT
    )
    size = models.IntegerField()
    description = models.TextField()
    maintenance_cost = models.IntegerField()
    status = models.IntegerField(
        choices=StatusType.choices, default=StatusType.AVAILABLE
    )


class PreferredProperty(models.Model):

    city = models.CharField(max_length=5)
    district = models.CharField(max_length=3)
    zone = models.CharField(max_length=3)
    property_type = models.IntegerField(choices=PropertyType.choices)
    detailed_type = models.IntegerField(choices=DetailedType.choices)
    budget_from = models.IntegerField()
    budget_to = models.IntegerField()
    description = models.TextField()
