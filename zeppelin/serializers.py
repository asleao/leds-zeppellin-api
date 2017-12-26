from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializer(serializers.ModelSerializer):
    """A serializer for our User objects."""

    class Meta:
        model = User
        fields = ('id', 'username')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

    def create(self, validated_data):
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError("A User with this username already exists")
        return User.objects.create(**validated_data)


class ToolSerializer(serializers.ModelSerializer):
    """A serializer for our Tool objects."""

    class Meta:
        model = models.Tool
        fields = ('id', 'name')
        extra_kwargs = {
            'name': {
                'validators': [],
            }
        }

    def create(self, validated_data):
        if models.Tool.objects.filter(name=self.validated_data['name']).exists():
            raise serializers.ValidationError("A Tool with this name already exists")
        return models.Tool.objects.create(**validated_data)


class LanguageSerializer(serializers.ModelSerializer):
    """A serializer for our Language objects."""

    class Meta:
        model = models.Language
        fields = ('id', 'name')
        extra_kwargs = {
            'name': {
                'validators': [],
            }
        }

    def create(self, validated_data):
        if models.Language.objects.filter(name=self.validated_data['name']).exists():
            raise serializers.ValidationError("A Language with this name already exists")
        return models.Language.objects.create(**validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    """A serializer for our Project objects."""

    tools = ToolSerializer(many=True)
    team = UserSerializer(many=True)
    owner = UserSerializer()
    language = LanguageSerializer()

    class Meta:
        model = models.Project
        fields = ('id', 'name', 'tools', 'team', 'owner', 'language')

    def create(self, validated_data):

        tool_data = validated_data.pop('tools')
        team_data = validated_data.pop('team')
        owner_data = validated_data.pop('owner')
        language_data = validated_data.pop('language')

        owner = User.objects.get(username=owner_data['username'])
        language = models.Language.objects.get(name=language_data['name'])

        project = models.Project.objects.create(owner=owner, language=language, **validated_data)

        for tool in tool_data:
            tool = models.Tool.objects.get(name=tool['name'])
            project.tools.add(tool.id)

        for team in team_data:
            team = User.objects.get(username=team['username'])
            project.team.add(team.id)

        project.save()

        return project
