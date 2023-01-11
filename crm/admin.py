from django.contrib import admin

from .models import Project, Address, City

admin.site.register(City)
admin.site.register(Address)
admin.site.register(Project)