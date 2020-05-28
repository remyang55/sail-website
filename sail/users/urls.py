from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('register/teachers', views.register_teacher, name='users-register-teacher'),
    path('register/students', views.register_student, name='users-register-student'),
    path('profile/', views.profile, name='users-profile'),
]
