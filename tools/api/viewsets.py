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

    # TODO implement patch
    @action(methods=['post', 'patch'], detail=True)
    def credential(self, request, id):
        if request.method == 'POST':
            owner = User.objects.get(pk=request.data['owner_id'])
            username = request.data['username']
            token = request.data['token']

            credential = ToolCredential.objects.filter(owner=owner, tool_id=id)
            # TODO test more cases of validation
            if credential.exists():
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={
                                    "detail": "This tool already have credentials, you should do a PATCH instead of "
                                              "POST."})

            if not username:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"detail": "Username field is required."})

            if not token:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"detail": "Token field is required."})

            toolcredential = ToolCredential(owner=owner,
                                            tool_id=id,
                                            password=password,
                                            token=token)
            toolcredential.save()

            return Response(status=status.HTTP_201_CREATED)
