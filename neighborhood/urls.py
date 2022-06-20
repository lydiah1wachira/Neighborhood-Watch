from . import views
from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
      
    path('', views.index, name='index'),
     path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
       
]