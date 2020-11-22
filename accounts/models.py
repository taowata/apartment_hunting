from django.db import models
from django.contrib.auth.models import AbstractUser

from apartment.models import Apartment


class User(AbstractUser):
    favorite_apartment = models.ManyToManyField(Apartment, blank=True)
