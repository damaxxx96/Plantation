from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Tree
from django.contrib.auth.decorators import login_required
import json


from django.http import JsonResponse
from .models import Tree


@login_required
def get_all_trees(request):
    try:
        trees = Tree.objects.all()
        tree_data = [{"species": tree.species} for tree in trees]
        return JsonResponse({"trees": tree_data})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def info_tree(request, tree_id):
    try:
        tree = Tree.objects.get(id=tree_id)
        tree_data = {"species": tree.species, "height": tree.height, "age": tree.age}
        return JsonResponse({"tree": tree_data})
    except Tree.DoesNotExist:
        return JsonResponse({"error": "Tree not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def create_tree(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            species = data.get("species")

            if not species:
                return JsonResponse({"error": "Species is required"}, status=400)

            height = data.get("height")
            age = data.get("age")

            tree = Tree(species=species, height=height, age=age)
            tree.save()

            return HttpResponse(status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponse(status=405)


@login_required
def update_tree(request, tree_id):
    try:
        tree = Tree.objects.get(pk=tree_id)
        data = json.loads(request.body)

        if "species" in data:
            tree.species = data["species"]
        if "height" in data:
            tree.height = data["height"]
        if "age" in data:
            tree.age = data["age"]

        tree.save()

    except Tree.DoesNotExist:
        return JsonResponse({"error": "Tree not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Tree updated successfully"}, status=200)


@login_required
def delete_tree(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            tree_id = data.get("tree_id")

            if not tree_id:
                return JsonResponse({"error": "Tree ID is required"}, status=400)

            try:
                tree = Tree.objects.get(id=tree_id)
                tree.delete()
                return JsonResponse({"message": "Tree deleted successfully"})
            except Tree.DoesNotExist:
                return JsonResponse({"error": "Tree not found"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
