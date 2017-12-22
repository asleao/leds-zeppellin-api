from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    """A serializer for our User objects."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ToolSerializer(serializers.ModelSerializer):
    """A serializer for our Tool objects."""

    class Meta:
        model = models.Tool
        fields = ('id', 'name')


class LanguageSerializer(serializers.ModelSerializer):
    """A serializer for our Language objects."""

    class Meta:
        model = models.Language
        fields = ('id', 'name')


class ProjectSerializer(serializers.ModelSerializer):
    """A serializer for our Project objects."""

    tools = serializers.SlugRelatedField(
        many=True,
        queryset=models.Tool.objects.all(),
        slug_field='name'
    )
    team = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = models.Project
        fields = ('id', 'name', 'tools', 'team', 'owner', 'language')
