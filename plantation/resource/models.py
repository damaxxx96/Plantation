from django.db import models


class Fertilizer(models.Model):
    amount = models.IntegerField()
    AVAILABILITY_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]


class Seed(models.Model):
    amount = models.IntegerField()
    AVAILABILITY_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]


class Tool(models.Model):
    amount = models.IntegerField()
    AVAILABILITY_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]
