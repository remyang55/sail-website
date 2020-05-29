from django.urls import path
from .views import (CourseListView, 
                    CourseDetailView,
                    CourseCreateView,
                    CourseUpdateView,
)
from . import views

urlpatterns = [
    path('', CourseListView.as_view(), name='courses_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='courses_detail'),
    path('create/', CourseCreateView.as_view(), name='courses_create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='courses_update'),
]
