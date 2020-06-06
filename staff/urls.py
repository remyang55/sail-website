from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_actions, name='staff_actions'),
    path('send-email/', views.send_email, name='staff_send_email')
]