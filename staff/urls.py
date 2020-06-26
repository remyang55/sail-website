from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_actions, name='staff-actions'),
    path('send-email/', views.send_email, name='staff-send-email')
]