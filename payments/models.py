from django.db import models

class Payment(models.Model):
    amount = models.FloatField()
    currency = models.CharField(max_length=3)
    stripe_payment_id = models.CharField(max_length=50)