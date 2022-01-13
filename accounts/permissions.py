from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """
    Custom permission to allow managers to access and modifi all CRM data
    """
    def has_permission(self, request, view):
        return request.user.department == "MANAGEMENT"

    def has_object_permission(self, request, view, obj):
        return request.user.department == "MANAGEMENT"
