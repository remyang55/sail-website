from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.unregister(Site)
