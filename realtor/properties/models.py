from django.db import models
# from realtor.properteis.enums import PropertyType


class Property(models.Model):

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

    image = models.CharField(max_length=50)
    price = models.IntegerField()
    address = models.CharField(max_length=30) # city, district, detailed_ 
    property_type = models.IntegerField(choices = PropertyType.choices)
    detailed_type = models.IntegerField(choices = DetailedType.choices)
    size = models.IntegerField()
    description = models.TextField()
    maintenance_cost = models.IntegerField()
    status = models.IntegerField(choices = StatusType.choices) 




