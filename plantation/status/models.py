from tree.views import Tree
from django.db import models
from plant.views import Plant


class Status(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="statuses")
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name="statuses")
    last_watered = models.DateTimeField(null=True, blank=True)
