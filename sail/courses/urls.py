from django.urls import path
from .views import CourseListView
from . import views

urlpatterns = [
    path('', CourseListView.as_view(), name='courses_list'),
]
