from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)
from .models import Course, Section
from .forms import TagForm, TimeForm

import datetime

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_form'] = TagForm(initial=self.get_initial())
        context['time_form'] = TimeForm(initial=self.get_initial())
        context['title'] = 'Courses'
        return context
    
    def get_initial(self):
        if self.request.method == 'GET':
            initial = {}
            initial['tags'] = self.request.GET.getlist('tags')
            initial['times'] = self.request.GET.getlist('times')
            return initial
        return super().get_initial()
    
    def get_queryset(self):
        selected_tags = self.request.GET.getlist('tags')
        selected_times = self.request.GET.getlist('times')
        course_name_contains = self.request.GET.get('course_name_contains')
        description_contains = self.request.GET.get('description_contains')

        queryset = Course.objects.all()

        if course_name_contains != '' and course_name_contains is not None:
            queryset = queryset.filter(course_name__icontains=course_name_contains)
        
        if description_contains != '' and description_contains is not None:
            queryset = queryset.filter(description__icontains=description_contains)

        if len(selected_tags) != 0:
            for tag in selected_tags:
                queryset = queryset.filter(tags__name=tag)
        
        if len(selected_times) != 0:
            for time in selected_times:
                queryset = queryset.filter(section__start_time__time=datetime.datetime.strptime(time, "%H:%M").time())
        
        return queryset
    
    def post(self, request, *args, **kwargs):
        if self.request.user.role == get_user_model().STUDENT:
            for section_id, action in request.POST.items():
                if action == 'Register':

                    # s stands for section, rs stands for already registered section
                    s = Section.objects.get(pk=section_id)

                    if (s.students.all().count() >= s.room.max_capacity
                        or (s.course.capacity_limit is not None and s.students.all().count() >= s.course.capacity_limit)):
                        messages.warning(request, 'Cannot Register: Section is full')
                        return redirect('courses_list')

                    for rs in self.request.user.student.section_set.all():
                        if s.course == rs.course:
                            messages.warning(request, 'Cannot Register: Already registered for another section of the same course')
                            return redirect('courses_list')
                        
                        if ((s.start_time == rs.start_time)
                            or (s.start_time < rs.start_time
                                and s.start_time + s.course.course_duration > rs.start_time)
                            or (s.start_time > rs.start_time
                                and rs.start_time + rs.course.course_duration > s.start_time)):
                            messages.warning(request, 'Cannot Register: Time Conflict')
                            return redirect('courses_list')

                    self.request.user.student.section_set.add(section_id)
                elif action == 'Unregister':
                    self.request.user.student.section_set.remove(section_id)
        return redirect('courses_list')

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Course - {self.get_object()}'
        return context

    def post(self, request, *args, **kwargs):
        if self.request.user.role == get_user_model().STUDENT:
            for section_id, action in request.POST.items():
                if action == 'Register':

                    # s stands for section, rs stands for already registered section
                    s = Section.objects.get(pk=section_id)

                    if ((s.students.all().count() >= s.room.max_capacity)
                        or (s.course.capacity_limit is not None and s.students.all().count() >= s.course.capacity_limit)):
                        messages.warning(request, 'Cannot Register: Section is full')
                        return redirect('courses_list')

                    for rs in self.request.user.student.section_set.all():
                        if s.course == rs.course:
                            messages.warning(request, 'Cannot Register: Already registered for another section of the same course')
                            return redirect('courses_list')
                        
                        if ((s.start_time == rs.start_time)
                            or (s.start_time < rs.start_time
                                and s.start_time + s.course.course_duration > rs.start_time)
                            or (s.start_time > rs.start_time
                                and rs.start_time + rs.course.course_duration > s.start_time)):
                            messages.warning(request, 'Cannot Register: Time Conflict')
                            return redirect('courses_list')

                    self.request.user.student.section_set.add(section_id)
                elif action == 'Unregister':
                    self.request.user.student.section_set.remove(section_id)
        return redirect('courses_list')

class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    context_object_name = 'course'
    fields = ['course_name', 'short_description', 'description',
              'prior_knowledge', 'course_length', 'capacity_limit'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Course'
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Course - {self.get_object()}'
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete Course - {self.get_object()}'
        return context

    def test_func(self):
        course = self.get_object()
        return (self.request.user.role == get_user_model().TEACHER
            and self.request.user.teacher == course.teacher)

@login_required
@user_passes_test(lambda user: user.role == get_user_model().STUDENT)
def student_courses(request):
    ordered_sections = request.user.student.section_set.order_by('start_time')
    return render(request, 'courses/my_courses.html', {'sections':ordered_sections, 'title':'My Courses'})
