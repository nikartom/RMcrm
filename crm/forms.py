from django import forms
from crispy_forms.layout import Layout, Field, BaseInput
from crispy_forms.helper import FormHelper
from .models import *


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["city", "street", "numb"]

    def __init__(self, *args, **kwargs):
        city = kwargs.pop("city", "")
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields["city"] = forms.ModelChoiceField(queryset=City.objects.all(), label='Город')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["file", "sq", "rent_tax"]


class ProjectDetailForm(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        exclude = ['project', 'comment', 'resume', 'complite', 'created_at']

        