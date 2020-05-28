from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sail_home'),
    path('about/', views.about, name='sail_about'),
    path('staff/', views.staff, name='sail_staff'),
]
