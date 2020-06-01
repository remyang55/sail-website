from django.db import models
from django.urls import reverse
from users.models import Teacher, Student
from taggit.managers import TaggableManager

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    
    course_name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, help_text="Students will see this description when they scroll through all the available courses.")
    description = models.TextField()
    prior_knowledge = models.CharField(max_length=100, blank=True, help_text="Leave blank if none.")
    course_length = models.PositiveSmallIntegerField(default=60)
    capacity_limit = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Leave blank if none.")
    approved = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.course_name
    
    def get_absolute_url(self):
        return reverse('courses_detail', kwargs={'pk': self.pk})
