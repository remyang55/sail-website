from django.db import models
from django.urls import reverse
from users.models import Teacher

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    prior_knowledge = models.CharField(max_length=100, blank=True)
    course_length = models.PositiveSmallIntegerField(default=60)
    capacity_limit = models.PositiveSmallIntegerField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name
    
    def get_absolute_url(self):
        return reverse('courses_detail', kwargs={'pk': self.pk})
