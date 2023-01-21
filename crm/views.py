from django.http import HttpResponseRedirect
from django.shortcuts import  render, redirect
from django.urls import reverse
from django_tables2 import RequestConfig, Table
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import DefaultStorage
from django.views.generic import ListView

from .forms import *
from .filters import *
from .models import *



def homepage(request):
    return render(request=request, template_name="index.html")


class TableAll(Table):
    class Meta:
        model = Project
        attrs = {"class": "table table-striped table-bordered", "id": "TableToExport"}


def table(request):
    table = TableAll(Project.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "table.html", {"table": table})
      

def add_project(request):
    form_address = AddressForm(request.POST or None)
    form_project = ProjectForm(request.POST or None)
    form_detail = ProjectDetailForm(request.POST or None)

    if request.method == 'POST':
        if form_address.is_valid() and form_project.is_valid() and form_detail.is_valid():
            address_clean = form_address.cleaned_data
            project_clean = form_project.cleaned_data
            detail_clean = form_detail.cleaned_data
            a = Address.objects.update_or_create(**address_clean)
            p = Project.objects.update_or_create(
                address = a[0],
                manager = request.user,
                file = project_clean['file'],
                sq = project_clean['sq'],
                rent_tax = project_clean['rent_tax']
            )
            ProjectDetail.objects.create(
                project = p[0],
                **detail_clean
            )
            # return HttpResponseRedirect(reverse('crm:homepage'))
            return redirect("crm:homepage")

    context = {'form_address':form_address, 'form_project':form_project, 'form_detail':form_detail,}

    return render(request, 'crm/add_project.html', context)


class ProjectList(ListView):
    model = Project
    f = ProjectFilter()
    template_name = 'crm/project_list.html'
