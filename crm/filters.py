import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'sq': ['lt', 'gt'],
            'created_at': ['exact', 'year__gt']
        }