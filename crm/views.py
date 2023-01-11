from django.shortcuts import render

from .models import Project

def homepage(request):
    	return render(request=request, template_name='index.html')
