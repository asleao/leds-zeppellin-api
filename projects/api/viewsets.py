from rest_framework.viewsets import ModelViewSet

from projects.api.serializers import ProjectSerializer
from projects.models import Project


class ProjectViewSet(ModelViewSet):
    """Handle creating, reading and updating Project"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_fields = ('owner', 'language')
