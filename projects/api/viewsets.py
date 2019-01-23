from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from projects.api.serializers import ProjectSerializer
from projects.models import Project
from tools.views import tools_without_credentials


class ProjectViewSet(ModelViewSet):
    """Handle creating, reading and updating Project"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_fields = ('owner', 'language')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JWTAuthentication,)
    lookup_field = 'id'

    @action(methods=['post'], detail=True)
    def tools(self, request, id):
        tools = request.data['tools']
        project = Project.objects.get(id=id)
        tools_pending_credentials = tools_without_credentials(project.owner, tools)
        if len(tools_pending_credentials) > 0:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"detail": "Owner need tool credentials.",
                                  "tools_pending_credentials": tools_pending_credentials})
        else:
            project.tools.set(tools)
            project.save()
            return Response(status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True)
    def team(self, request, id):
        team = request.data['team']

        project = Project.objects.get(id=id)

        project.team.set(team)

        project.save()
        # TODO:tratar erros
        return Response(status=status.HTTP_201_CREATED)
