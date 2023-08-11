from django.urls import path
from . import views


urlpatterns = [
    # ...
    path("get-all-plants/", views.get_all_plants, name="get_all_plants"),
    path("<int:plant_id>/info", views.info_plant, name="info_plant"),
    path("deleteplant/", views.delete_plant, name="delete_plant"),
    path("create/", views.create_plant, name="plant"),
    path("update/<int:plant_id>", views.update_plant, name="update_plant"),
]
