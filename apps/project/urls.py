#
# Import Django

from django.urls import path


#
# Import views

from .views import projects


#
# Url pattern

app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),
]