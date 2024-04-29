from django.db import models


class PropertyType(models.IntegerChoices):
    PURCHASE = 1
    LONGTERM = 2
    MONTHLY = 3


class DetailedType(models.IntegerChoices):
    ONE_ROOM = 1
    TWO_ROOM = 2
    OFFICETEL = 3
    APARTMENT = 4


class StatusType(models.IntegerChoices):
    AVAILABLE = 1
    IN_PROGRESS = 2
    DONE = 3
