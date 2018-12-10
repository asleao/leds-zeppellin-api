from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.state import User

from authentications.api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Handle creating, reading and updating User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
