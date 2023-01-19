from django.urls import path

from . import views

app_name = "crm"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("table/", views.table, name="table"),
    path("add_project/", views.AddProjectWizard.as_view(views.FORMS), name="add_project"),
]
