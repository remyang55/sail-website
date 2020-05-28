from django.urls import path
from .views import (CourseListView, 
                    CourseDetailView,
)
from . import views

urlpatterns = [
    path('', CourseListView.as_view(), name='courses_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='courses_detail'),
]
