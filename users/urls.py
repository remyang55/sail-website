from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users_register'),
    path('register/teachers/', views.register_teacher, name='users_register_teacher'),
    path('register/students/', views.register_student, name='users_register_student'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='users_activate'),
    path('profile/', views.profile, name='users_profile'),
    path('forms/', views.forms, name='users_forms'),
    path('forms/medical-form', views.medical_form_pdf, name='users_forms_medical'),
]
