from django.urls import path
from . import views

urlpatterns = [
    path(
        "total-trees-and-plants/",
        views.total_trees_and_plants,
        name="total_trees_and_plants",
    ),
    path("average-health/", views.average_health, name="average_health"),
]
