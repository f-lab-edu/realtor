from django.db import models
from users.models import User


class Agent(User):

    rating = models.DecimalField(decimal_places=1, max_digits=2)


class Contract(models.Model):

    mortgage_ratio = models.DecimalField(decimal_places=2, max_digits=4)
    down_payment = models.IntegerField()
    agreements = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
