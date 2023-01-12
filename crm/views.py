from django.shortcuts import render
from django_tables2 import Column, RequestConfig, Table

from .models import Project

def homepage(request):
    	return render(request=request, template_name='index.html')


class TableAll(Table):
	class Meta:
		model = Project
		attrs = {'class': 'table table-striped table-bordered', 'id':'TableToExport'}

def table(request):
	table = TableAll(Project.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'table.html', {'table': table})
