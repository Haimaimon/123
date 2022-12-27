from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
    path('register/', views.registerPage,name="register"),
]