from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from languages.api.serializers import LanguageSerializer
from languages.models import Language


class LanguageViewSet(ModelViewSet):
    """Handle creating, reading and updating Language"""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticated,)
