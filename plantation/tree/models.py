from django.db import models


class Tree(models.Model):
    HEALTH_CHOICES = [
        ("good", "Good"),
        ("average", "Average"),
        ("poor", "Poor"),
    ]

    species = models.CharField(max_length=100)
    height = models.FloatField()
    age = models.IntegerField()
    health = models.CharField(max_length=10, choices=HEALTH_CHOICES, default="average")
