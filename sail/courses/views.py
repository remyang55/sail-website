from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
)
from .models import Course

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'

class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    context_object_name = 'course'
    fields = ['course_name', 'short_description', 'description',
              'prior_knowledge', 'course_length', 'capacity_limit'
    ]

    def test_func(self):
        return self.request.user.role == get_user_model().TEACHER

    def form_valid(self, form):
        form.instance.save()
        form.instance.teachers.add(self.request.user.teacher)
        return super().form_valid(form)

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    context_object_name = 'course'
    fields = ['course_name', 'short_description', 'description',
              'prior_knowledge', 'course_length', 'capacity_limit'
    ]

    def test_func(self):
        course = self.get_object()
        return (self.request.user.role == get_user_model().TEACHER
            and self.request.user.teacher == course.teacher)

    def form_valid(self, form):
        form.instance.save()
        form.instance.teachers.add(self.request.user.teacher)
        return super().form_valid(form)
