from django.http import HttpRequest, HttpResponse, JsonResponse

from decorators.custom_login_decorator import custom_login_required
from helpers.auth_helper import retrieve_user
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json


@login_required
def get_all_employees(request):
    try:
        employees = Employee.objects.all()
        employee_data = [
            {"name": employee.name, "job": employee.job} for employee in employees
        ]
        return JsonResponse({"employees": employee_data})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def info_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        employee_data = {
            "name": employee.name,
            "job": employee.job,
        }
        return JsonResponse(employee_data)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def delete_employee(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            employee_id = data.get("employee_id")

            if not employee_id:
                return JsonResponse({"error": "Employee ID is required"}, status=400)

            try:
                employee = Employee.objects.get(id=employee_id)
                employee.delete()
                return JsonResponse({"message": "Employee deleted successfully"})
            except Employee.DoesNotExist:
                return JsonResponse({"error": "Employee not found"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@custom_login_required
def create_employee(request):
    if request.method == "POST":
        try:
            user = retrieve_user(request)
            employee = Employee.objects.filter(user=user).first()

            if not employee:
                return JsonResponse({"error": "You are not employed"}, status=403)

            if employee.job != "manager":
                return JsonResponse({"error": "You are not a manager"}, status=403)

            data = json.loads(request.body)
            name = data.get("name")

            if not name:
                return JsonResponse({"error": "Name is required"}, status=400)

            job = data.get("job")

            username = data.get("username")

            user_for_employee = User.objects.filter(username=username).first()

            if not user_for_employee:
                return JsonResponse({"error": "Username does not exist"}, status=400)

            employee = Employee(name=name, job=job, user=user_for_employee)
            employee.save()

            return HttpResponse(status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponse(status=405)


@login_required
def update_employee(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        data = json.loads(request.body)

        if "name" in data:
            employee.name = data["name"]
        if "job" in data:
            employee.job = data["job"]

        employee.save()

    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Employee updated successfully"}, status=200)


@custom_login_required
def info_employee_self(request):
    try:
        user = retrieve_user(request)
        employee = Employee.objects.get(user=user)
        employee_data = {
            "name": employee.name,
            "job": employee.job,
        }
        return JsonResponse(employee_data)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
