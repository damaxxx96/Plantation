from django.urls import path
from . import views

urlpatterns = [
    path("registation/", views.registration, name="registration"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("deleteprofile/", views.delete_account, name="delete_profile"),
    path("changepassword/", views.change_password, name="change_password"),
]
