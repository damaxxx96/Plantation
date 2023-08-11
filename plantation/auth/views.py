from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json


@csrf_exempt
def registration(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data["username"]
            password = data["password"]

            new_user = User(username=username, password=password)
            new_user.set_password(password)
            new_user.save()

            return JsonResponse({"message": "Registration successful"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data["username"]
            password = data["password"]

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Login successful"})
            else:
                return JsonResponse(
                    {"error": "Invalid username or password"}, status=401
                )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logout successful"})


@csrf_exempt
def delete_account(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data["username"]
            password = data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                user.delete()
                return JsonResponse({"message": "Account deleted successfully"})
            else:
                return JsonResponse(
                    {"error": "Invalid username or password"}, status=401
                )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@login_required
@csrf_exempt
def change_password(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            old_password = data["old_password"]
            new_password1 = data["new_password1"]
            new_password2 = data["new_password2"]

            if (
                request.user.check_password(old_password)
                and new_password1 == new_password2
            ):
                request.user.set_password(new_password1)
                request.user.save()
                return JsonResponse({"message": "Password changed successfully"})
            else:
                return JsonResponse({"error": "Password change failed"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
