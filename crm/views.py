from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django_tables2 import RequestConfig, Table
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import DefaultStorage

from .forms import *
from .models import *

FORMS = [
    ('address', AddressForm),
    ('project', ProjectForm),
    ('detail', ProjectDetailForm)
]

TEMPLATES = {
    'address': 'crm/address.html',
    'project': 'crm/project.html',
    'detail': 'crm/detail.html'
}

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
      

class AddProjectWizard(SessionWizardView):
    file_storage = DefaultStorage()
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
    
    def get_form_kwargs(self, step):
        if step == 0:
            return {'user': self.request.user}
        else:
            return {}
    
    def get_context_data(self, form, **kwargs):
        context = super(AddProjectWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'detail':
            context.update({'ok': 'True'})
        return context
    
    def done(self, form_list, **kwargs):
        address_form = form_list[0].cleaned_data
        project_form = form_list[1].cleaned_data
        detail_form = form_list[2].cleaned_data
        a = Address.objects.create(**address_form)
        p = Project.objects.create(
            address = a,
            manager = self.request.user,
            file = project_form['file'],
            sq = project_form['sq'],
            rent_tax = project_form['rent_tax']
        )
        c = ProjectDetail.objects.create(
            project = p,
            **detail_form
        )
        return HttpResponseRedirect(reverse('liststudent'))
