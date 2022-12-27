from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
    path('register/', views.registerPage,name="register"),
    path('profile/', views.my_profile, name="profile"),
    path('delete/<int:id>', views.delete, name="delete"),




]