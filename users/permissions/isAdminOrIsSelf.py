from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIsSelf(BasePermission):
    """Allow users to see their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to see their own profile."""
        return request.user.is_superuser or obj.id == request.user.id
