from django.contrib import admin
from .models import Course, Room, Section

admin.site.register(Room)
admin.site.register(Section)

def approve_course(modeladmin, request, queryset):
    queryset.update(approved=True)
approve_course.short_description = 'Approve course'

class CourseAdmin(admin.ModelAdmin):
    actions = [approve_course, ]

admin.site.register(Course, CourseAdmin)
