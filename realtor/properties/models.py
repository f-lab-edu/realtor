from django.db import models
from properties.enums import DetailedType, PropertyType, StatusType
from users.models import Agent, User


class City(models.Model):
    name = models.CharField(max_length=3)


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)


class Zone(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)


class Property(models.Model):

    image = models.CharField(max_length=50, blank=True, default="")
    price = models.IntegerField()
    property_type = models.IntegerField(choices=PropertyType.choices, default=PropertyType.PURCHASE)
    detailed_type = models.IntegerField(choices=DetailedType.choices, default=DetailedType.APARTMENT)
    size = models.IntegerField()
    description = models.TextField()
    maintenance_cost = models.IntegerField()
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.AVAILABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    agents = models.ManyToManyField(Agent)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Properties"
