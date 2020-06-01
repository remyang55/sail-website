from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)
from .models import Course
from .forms import TagForm

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['tag_form'] = TagForm()
        return context
    
    def get_queryset(self):
        selected_tags = self.request.GET.getlist('tags')

        if not selected_tags:
            return Course.objects.all()
        else:
            filtered_courses = Course.objects.all()
            for tag in selected_tags:
                filtered_courses = filtered_courses.filter(tags__name=tag)
            return filtered_courses

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
        form.instance.teacher = self.request.user.teacher
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
        form.instance.teacher = self.request.user.teacher
        return super().form_valid(form)

class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    context_object_name = 'course'
    success_url = "/"

    def test_func(self):
        course = self.get_object()
        return (self.request.user.role == get_user_model().TEACHER
            and self.request.user.teacher == course.teacher)
