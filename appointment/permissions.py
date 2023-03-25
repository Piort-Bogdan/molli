from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """
    Allows access only to authenticated and staff users .
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)
