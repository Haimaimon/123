from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
    path('register/', views.registerPage,name="register"),
    path('profile/', views.my_profile, name="profile"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('studentjob/', views.studentjobs, name="studentjob"),
    path('add/', views.add, name= "add"),
    path('<int:id>', views.view_jobs, name="view_jobs"),
    path('index/', views.index, name="index"),
    path('logout/', views.logoutUser, name="logout"),




]