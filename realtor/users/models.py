from django.contrib.auth.models import AbstractUser
from django.db import models
from properties.enums import DetailedType, PropertyType


class User(AbstractUser):

    phone = models.CharField(max_length=12)


class Application(models.Model):
    class StatusType(models.IntegerChoices):
        SUBMITTED = 1
        CHECKING = 2
        ACCEPTED = 3

    status = models.IntegerField(choices=StatusType.choices)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    agent = models.ForeignKey("transactions.Agent", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class PreferredProperty(models.Model):

    city = models.CharField(max_length=5)
    district = models.CharField(max_length=3)
    zone = models.CharField(max_length=3)
    property_type = models.IntegerField(choices=PropertyType.choices)
    detailed_type = models.IntegerField(choices=DetailedType.choices)
    budget_from = models.IntegerField()
    budget_to = models.IntegerField()
    description = models.TextField()
    users = models.ManyToManyField(User)
