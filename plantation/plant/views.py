from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Plant
from django.contrib.auth.decorators import login_required
import json


from django.http import JsonResponse
from .models import Plant


@login_required
def get_all_plants(request):
    try:
        plants = Plant.objects.all()
        plant_data = [{"species": plant.species} for plant in plants]
        return JsonResponse({"plants": plant_data})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def info_plant(request, plant_id):
    try:
        plant = Plant.objects.get(id=plant_id)
        plant_data = {
            "species": plant.species,
            "height": plant.height,
            "age": plant.age,
            "health": plant.health,
        }
        return JsonResponse({"plant": plant_data})
    except Plant.DoesNotExist:
        return JsonResponse({"error": "Plant not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def delete_plant(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            plant_id = data.get("plant_id")

            if not plant_id:
                return JsonResponse({"error": "Plant ID is required"}, status=400)

            try:
                plant = Plant.objects.get(id=plant_id)
                plant.delete()
                return JsonResponse({"message": "Plant deleted successfully"})
            except Plant.DoesNotExist:
                return JsonResponse({"error": "Plant not found"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@login_required
def create_plant(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            species = data.get("species")

            if not species:
                return JsonResponse({"error": "Species is required"}, status=400)

            height = data.get("height")
            age = data.get("age")
            health = data.get("health")  # Add this line to get the health field

            plant = Plant(
                species=species, height=height, age=age, health=health
            )  # Include health
            plant.save()

            return HttpResponse(status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponse(status=405)


@login_required
def update_plant(request, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        data = json.loads(request.body)

        if "species" in data:
            plant.species = data["species"]
        if "height" in data:
            plant.height = data["height"]
        if "age" in data:
            plant.age = data["age"]
        if "health" in data:
            plant.health = data["health"]

        plant.save()

    except Plant.DoesNotExist:
        return JsonResponse({"error": "Plant not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Plant updated successfully"}, status=200)
