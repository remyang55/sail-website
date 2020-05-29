from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
)
from .models import Course

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    context_object_name = 'course'
    fields = ['course_name', 'short_description', 'description',
              'prior_knowledge', 'course_length', 'capacity_limit'
    ]

    def form_valid(self, form):
        form.instance.save()
        form.instance.teachers.add(self.request.user.teacher)
        return super().form_valid(form)
