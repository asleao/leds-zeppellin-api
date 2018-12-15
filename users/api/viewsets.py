from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.state import User

from users.api.serializers import UserSerializer
from users.permissions.isAdminOrIsSelf import IsAdminOrIsSelf


class UserViewSet(ModelViewSet):
    """Handle creating, reading and updating User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminOrIsSelf]
        return [permission() for permission in permission_classes]

    # TODO Criar action para admin e adicionar permissões ao endpoint.
