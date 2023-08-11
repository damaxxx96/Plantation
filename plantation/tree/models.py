from django.db import models


class Tree(models.Model):
    species = models.CharField(max_length=100)
    height = models.FloatField()
    age = models.IntegerField()
