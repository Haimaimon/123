from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



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
    path('jobseeker/', views.userPage, name='jobseeker'),
    path('profileseeker/', views.profileseeker, name="profileseeker"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
]