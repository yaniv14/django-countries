from django.db import models
from django_countries.fields import CountryField


class Person(models.Model):
    name = models.CharField(max_length=50)
    country = CountryField(blank=True)
    other_country = CountryField(
        blank=True, flag_static_url='//flags.example.com/')
