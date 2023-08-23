from django.urls import path
from . import views


urlpatterns = [
    # ...
    path("get-all-employees/", views.get_all_employees, name="get_all_employees"),
    path("<int:employee_id>/info", views.info_employee, name="info_employee"),
    path("info/self", views.info_employee_self, name="info_employee_self"),
    path("deleteemployee/", views.delete_employee, name="delete_employee"),
    path("create/", views.create_employee, name="employee"),
    path("update/<int:employee_id>", views.update_employee, name="update_employee"),
]
