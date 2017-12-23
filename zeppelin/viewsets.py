
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import permissions
from . import serializers
from . import models


class ToolViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating Tools"""

    serializer_class = serializers.ToolSerializer
    queryset = models.Tool.objects.all()
    authentication_classes = (TokenAuthentication,)


class LanguageViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating Language"""

    serializer_class = serializers.LanguageSerializer
    queryset = models.Language.objects.all()
    authentication_classes = (TokenAuthentication,)


class ProjectViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating Project"""

    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()
    authentication_classes = (TokenAuthentication,)

    @detail_route()
    def team(self, request, pk=None):
        """
        Returns a list of all the team members from the specified project.
        """
        project = self.get_object()

        return Response([member.username for member in project.team.all()])

    @detail_route()
    def tools(self, request, pk=None):
        """
        Returns a list of all the tools from the specified project.
        """
        project = self.get_object()

        return Response([tool.name for tool in project.tools.all()])
