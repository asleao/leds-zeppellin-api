from rest_framework.serializers import ModelSerializer

from projects.models import Project


class ProjectSerializer(ModelSerializer):
    """A serializer for our Project objects."""

    class Meta:
        model = Project
        fields = ['id', 'name', 'tools', 'team', 'owner', 'language']
