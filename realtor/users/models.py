from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone = models.CharField(max_length=12)

 
class Agent(User):

    rating = models.DecimalField(decimal_places=1, max_digits=1)