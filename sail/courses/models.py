from django.db import models
from django.urls import reverse
from users.models import Teacher, Student
from taggit.managers import TaggableManager

import datetime

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    
    course_name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, help_text="Students will see this description when they scroll through all the available courses.")
    description = models.TextField()
    prior_knowledge = models.CharField(max_length=100, blank=True, help_text="Leave blank if none.")
    course_length = models.PositiveSmallIntegerField(default=60, help_text="Length of your course in minutes, either 60 or 120.")
    capacity_limit = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Leave blank if none.")
    approved = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    @property
    def course_duration(self):
        return datetime.timedelta(minutes=self.course_length)

    class Meta:
        ordering = ["course_name"]

    def __str__(self):
        return self.course_name
    
    def get_absolute_url(self):
        return reverse('courses_detail', kwargs={'pk':self.pk})

class Room(models.Model):
    room_name = models.CharField(max_length=20)
    max_capacity = models.PositiveSmallIntegerField(default=20)

    def __str__(self):
        return self.room_name

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.course}, {self.start_time.strftime("%H:%M")}'
