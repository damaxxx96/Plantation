from django.http import JsonResponse

from .models import Plant, Tree, Status
from django.utils import timezone


def total_trees_and_plants(request):
    total_tree_count = Tree.objects.count()
    total_plant_count = Plant.objects.count()

    all_trees = Tree.objects.all()
    all_plants = Plant.objects.all()

    total_tree_height = sum(tree.height for tree in all_trees)
    total_tree_age = sum(tree.age for tree in all_trees)
    average_tree_height = (
        total_tree_height / total_tree_count if total_tree_count > 0 else 0
    )
    average_tree_age = total_tree_age / total_tree_count if total_tree_count > 0 else 0

    total_plant_height = sum(plant.height for plant in all_plants)
    total_plant_age = sum(plant.age for plant in all_plants)
    average_plant_height = (
        total_plant_height / total_plant_count if total_plant_count > 0 else 0
    )
    average_plant_age = (
        total_plant_age / total_plant_count if total_plant_count > 0 else 0
    )

    data = {
        "total_tree_count": total_tree_count,
        "total_plant_count": total_plant_count,
        "average_tree_height": average_tree_height,
        "average_tree_age": average_tree_age,
        "average_plant_height": average_plant_height,
        "average_plant_age": average_plant_age,
    }

    return JsonResponse(data)


def calculate_average_health(items, health_field):
    health_counts = {"good": 0, "average": 0, "poor": 0}

    for item in items:
        health = getattr(item, health_field)
        health_counts[health] += 1

    average_health = (
        "good"
        if health_counts["good"] > health_counts["average"]
        and health_counts["good"] > health_counts["poor"]
        else "average"
        if health_counts["average"] > health_counts["good"]
        and health_counts["average"] > health_counts["poor"]
        else "poor"
    )

    return average_health


def average_health(request):
    all_trees = Tree.objects.all()
    all_plants = Plant.objects.all()

    average_tree_health = calculate_average_health(all_trees, "health")
    average_plant_health = calculate_average_health(all_plants, "health")

    data = {
        "average_tree_health": average_tree_health,
        "average_plant_health": average_plant_health,
    }

    return JsonResponse(data)
