from . import views
from django.urls import path,re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    
    path('', views.index, name='index')
]