from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users_register'),
    path('register/teachers/', views.register_teacher, name='users_register_teacher'),
    path('register/students/', views.register_student, name='users_register_student'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='users_activate'),
    path('profile/', views.profile, name='users_profile'),
]
