from rest_framework.serializers import ModelSerializer

from tools.models import Tool


class ToolSerializer(ModelSerializer):
    """A serializer for our Tool objects."""

    class Meta:
        model = Tool
        fields = ['id', 'name']
