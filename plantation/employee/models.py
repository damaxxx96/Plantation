from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    JOB_ROLES = [
        ("gardener", "Gardener"),
        ("arborist", "Arborist"),
        ("manager", "Manager"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=10, choices=JOB_ROLES, default="gardener")
