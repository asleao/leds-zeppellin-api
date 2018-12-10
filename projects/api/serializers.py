from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.state import User

from authentications.api.serializers import UserSerializer
from languages.api.serializers import LanguageSerializer
from languages.models import Language
from projects.models import Project
from tools.api.serializers import ToolSerializer


class ProjectSerializer(ModelSerializer):
    """A serializer for our Project objects."""
    tools = ToolSerializer(many=True, read_only=True)
    team = UserSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    owner_id = PrimaryKeyRelatedField(source='owner', queryset=User.objects.all(), write_only=True, )
    language = LanguageSerializer(read_only=True)
    language_id = PrimaryKeyRelatedField(source='language', queryset=Language.objects.all(), write_only=True, )

    class Meta:
        model = Project
        fields = ['id', 'name', 'tools', 'team', 'owner', 'owner_id', 'language', 'language_id']
