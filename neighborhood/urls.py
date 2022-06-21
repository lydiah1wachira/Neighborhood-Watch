from . import views
from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
      
    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('register/logout/', views.logoutUser, name = 'logout'),
    path('EditProfile/<username>/',views.EditProfile,name = 'EditProfile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('hood/', views.hood, name = 'hood'),
    path('estate/<int:id>/', views.estate, name = 'each-hood'),
       
]