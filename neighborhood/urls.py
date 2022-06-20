from . import views
from django.urls import path,re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path("register/", views.register_request, name="register"),
    path("register/login/", views.login, name="login"),
    path("logout", views.logout_request, name= "logout"),
    
    path('', views.index, name='index'),
    
   
]