from django.db import models


class Application(models.Model):

    class StatusType(models.IntegerChoices):
        SUBMITTED = 1
        CHECKING = 2
        ACCEPTED = 3

    status = models.IntegerField(choices = StatusType.choices)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Contract(models.Model):

    mortgage_ratio = models.DecimalField(decimal_places=2, max_digits=2)
    down_payment = models.IntegerField()
    agreements = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()



