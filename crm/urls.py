from django.urls import path
from . import views

app_name = "crm" 

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("table/", views.table, name="table"),
]