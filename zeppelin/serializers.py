from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from .models import *


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

    def update(self, instance, validated_data):
        instance.name = self.validated_data['username'] or instance.name
        instance.save()
        return instance


class ToolSerializer(serializers.ModelSerializer):
    """A serializer for our Tool objects."""

    class Meta:
        model = Tool
        fields = ('id', 'name')
        extra_kwargs = {
            'name': {
                'validators': [],
            }
        }

    def create(self, validated_data):
        if Tool.objects.filter(name=self.validated_data['name']).exists():
            raise serializers.ValidationError("A Tool with this name already exists")
        return Tool.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = self.validated_data['name'] or instance.name
        instance.save()
        return instance


class LanguageSerializer(serializers.ModelSerializer):
    """A serializer for our Language objects."""

    class Meta:
        model = Language
        fields = ('id', 'name')
        extra_kwargs = {
            'name': {
                'validators': [],
            }
        }

    def create(self, validated_data):
        if Language.objects.filter(name=self.validated_data['name']).exists():
            raise serializers.ValidationError("A Language with this name already exists")
        return Language.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = self.validated_data['name'] or instance.name
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    """A serializer for our Project objects."""

    tools = ToolSerializer(many=True)
    team = UserSerializer(many=True)
    owner = UserSerializer()
    language = LanguageSerializer()

    class Meta:
        model = Project
        fields = ('id', 'name', 'tools', 'team', 'owner', 'language')

    def create(self, validated_data):

        tool_data = validated_data.pop('tools')
        team_data = validated_data.pop('team')
        owner_data = validated_data.pop('owner')
        language_data = validated_data.pop('language')

        owner = User.objects.get(username=owner_data['username'])
        language = Language.objects.get(name=language_data['name'])

        project = Project.objects.create(owner=owner, language=language, **validated_data)

        for tool in tool_data:
            tool = Tool.objects.get(name=tool['name'])
            project.tools.add(tool.id)

        for team in team_data:
            team = User.objects.get(username=team['username'])
            project.team.add(team.id)

        project.save()

        return project

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.tools.clear()
        for tool in validated_data.get('tools', instance.tools):
            tool = Tool.objects.get(name=tool['name'])
            instance.tools.add(tool.id)

        instance.team.clear()
        for team in validated_data.get('team', instance.team):
            team = User.objects.get(username=team['username'])
            instance.team.add(team.id)

        owner_data = validated_data.pop('owner')
        language_data = validated_data.pop('language')

        instance.owner = User.objects.get(username=owner_data['username'])

        instance.language = Language.objects.get(name=language_data['name'])

        return instance
