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
            raise serializers.ValidationError(
                "A User with this username already exists")
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
            raise serializers.ValidationError(
                "A Tool with this name already exists")
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
            raise serializers.ValidationError(
                "A Language with this name already exists")
        return Language.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = self.validated_data['name'] or instance.name
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    """A serializer for our Project objects."""
    class Meta:
        model = Project
        fields = ('id', 'name', 'tools', 'team', 'owner', 'language')
