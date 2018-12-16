from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.state import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """A serializer for our User objects."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ('id',)
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']))
