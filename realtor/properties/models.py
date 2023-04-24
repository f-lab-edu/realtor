from django.db import models
from properties.enums import DetailedType, PropertyType, StatusType
from transactions.models import Agent
from users.models import User


class Property(models.Model):

    image = models.CharField(max_length=50, blank=True, default="")
    price = models.IntegerField()
    city = models.CharField(max_length=5)
    district = models.CharField(max_length=3)
    zone = models.CharField(max_length=3)
    property_type = models.IntegerField(choices=PropertyType.choices, default=PropertyType.PURCHASE)
    detailed_type = models.IntegerField(choices=DetailedType.choices, default=DetailedType.APARTMENT)
    size = models.IntegerField()
    description = models.TextField()
    maintenance_cost = models.IntegerField()
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.AVAILABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    agents = models.ManyToManyField(Agent)

    class Meta:
        verbose_name_plural = "Properties"
