from django.db import models


class User(models.Model):

    name = models.CharField(max_length=5)
    password = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=20)
    since = models.DateField(auto_now_add=True)

class Agent(User):
    rating = models.DecimalField(decimal_places=1)