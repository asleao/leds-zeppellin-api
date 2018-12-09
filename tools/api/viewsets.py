from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from tools.api.serializers import ToolSerializer
from tools.models import Tool


class ToolViewSet(ModelViewSet):
    """Handle creating, reading and updating Tool"""
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
