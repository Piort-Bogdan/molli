from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAOwnerAndAuthenticatedOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated or obj.owner == request.user
        )

