from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.state import User


class UserSerializer(ModelSerializer):
    """A serializer for our User objects."""

    class Meta:
        model = User
        fields = ['id', 'username']
