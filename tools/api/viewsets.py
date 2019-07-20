from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from tools.api.serializers import ToolSerializer
from tools.models import Tool, ToolCredential


class ToolViewSet(ModelViewSet):
    """Handle creating, reading and updating Tool"""
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    lookup_field = 'id'

    # TODO: finish validations
    @action(methods=['post'], detail=True)
    def credential(self, request, id):
        owner = User.objects.get(pk=request.data['owner_id'])
        username = request.data['username']
        password = request.data['password']
        token = request.data['token']

        if not token and not username and not password:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"detail": "A token or a username and password should be provided."})

        toolcredential = ToolCredential(owner=owner,
                                        tool_id=id,
                                        username=username,
                                        password=password,
                                        token=token)
        toolcredential.save()

        return Response(status=status.HTTP_201_CREATED)
