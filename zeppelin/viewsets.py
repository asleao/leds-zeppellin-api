
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

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
