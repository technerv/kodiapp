from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerPermission(BasePermission):
    def has_permission(self, request, format=None):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff and
            request.user.is_owner,
        )


class IsTenantPermission(BasePermission):
    def has_permission(self, request, format=None):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff and
            request.user.is_tenant,
        ) 