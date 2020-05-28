from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
)
from .models import Course

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
