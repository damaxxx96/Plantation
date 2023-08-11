from django.urls import path
from . import views

urlpatterns = [
    # ...
    path("get-all-trees/", views.get_all_trees, name="get_all_trees"),
    path("<int:tree_id>/info", views.info_tree, name="info_tree"),
    path("create/", views.create_tree, name="create"),
    path("update/<int:tree_id>", views.update_tree, name="update_tree"),
    path("deletetree/", views.delete_tree, name="delete_tree"),
]
