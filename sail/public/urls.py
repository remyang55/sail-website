from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sail-home'),
    path('about/', views.about, name='sail-about'),
]
