#
# Import Django

from django.contrib import admin


#
# Import models

from .models import Project


#
# Register

admin.site.register(Project)
