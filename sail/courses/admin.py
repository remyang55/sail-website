from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Course, Room, Section

admin.site.register(Room)
admin.site.register(Section)

def approve_course(modeladmin, request, queryset):
    queryset.update(approved=True)
approve_course.short_description = 'Approve selected courses'

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    actions = [approve_course, ]
