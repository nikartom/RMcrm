from django.contrib import admin

from .models import *

admin.site.register(City)
admin.site.register(Address)
admin.site.register(Project)
admin.site.register(ProjectDetail)