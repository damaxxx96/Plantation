from django.db import models

from django.db import models


class Plant(models.Model):
    species = models.CharField(max_length=100)
    height = models.FloatField()
    age = models.IntegerField()
