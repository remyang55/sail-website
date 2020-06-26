from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Course, Room, Section

admin.site.register(Room)
admin.site.register(Section)

""" Admin action to approve many courses at once """
def approve_course(modeladmin, request, queryset):
    queryset.update(approved=True)
approve_course.short_description = 'Approve selected courses'

""" Extending ImportExportModelAdmin allows us to export Course database data to a csv file """
@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    actions = [approve_course, ]
