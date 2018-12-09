from rest_framework.serializers import ModelSerializer

from languages.models import Language


class LanguageSerializer(ModelSerializer):
    """A serializer for our Language objects."""

    class Meta:
        model = Language
        fields = ['id', 'name']
