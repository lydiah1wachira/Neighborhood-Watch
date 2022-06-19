from . import views
from django.urls import path,re_path

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")
]