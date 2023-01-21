"""
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
        a = Address.objects.update_or_create(**address_form)
        p = Project.objects.create(
            address = a[0],
            manager = self.request.user,
            file = project_form['file'],
            sq = project_form['sq'],
            rent_tax = project_form['rent_tax']
        )
        c = ProjectDetail.objects.create(
            project = p,
            **detail_form
        )
        return HttpResponseRedirect(reverse('crm:homepage'))
"""