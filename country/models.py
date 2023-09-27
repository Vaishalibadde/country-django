from django.db import models

class Country(models.Model):
    country_name= models.CharField(max_length=100)
    country_currency = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    independence_date = models.CharField(max_length=100)
    description = models.TextField()
    short_name = models.CharField(max_length=100)
