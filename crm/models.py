from django.db import models
from django.contrib.auth.models import AbstractUser
from .items import REGIONS

class User(AbstractUser):
    region_field = models.CharField(max_length=256, choices=REGIONS, default='24', verbose_name="Регион")

    def __str__(self):
        return self.username
