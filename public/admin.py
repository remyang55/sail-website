from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

# These are registered by default in Django admin, but are irrelevant in our use case
admin.site.unregister(Group)
admin.site.unregister(Site)
