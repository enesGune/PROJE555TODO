from django.db import models

# Create your models here.


class Customer(models.Model):
    tc_no = models.CharField(max_length=12)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    town = models.CharField(max_length=120)
