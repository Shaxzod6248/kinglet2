from django.db import models
import os


class ShippingChoices(models.TextChoices):
    STANDARD = 'STANDARD', 'Standard'
    EXPRESS = 'EXPRESS', 'Express'


class Checkout_form(models.Model):
    name = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=70, null=True)
    postal = models.CharField(max_length=30, null=True)
    address = models.TextField(null=True)
    shipping = models.CharField(max_length=50, null=True)
    method = models.CharField(max_length=50, choices=ShippingChoices.choices, null=True)

    def __str__(self):
        return self.country