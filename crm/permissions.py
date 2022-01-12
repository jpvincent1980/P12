import logging

from rest_framework.permissions import BasePermission, SAFE_METHODS


logger = logging.getLogger(__name__)


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as an Adminuser, or is a read-only request.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser


class IsSalesContact(BasePermission):
    """
    Custom permission to allow sales contact to update their client,
    client's contract and client's event data
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        try:
            return obj.client.sales_contact == request.user
        except AttributeError:
            logger.exception("No attribute called sales_contact")
            return obj.sales_contact == request.user


class IsSupportContact(BasePermission):
    """
    Custom permission to allow support contact to update their assigned
    events' data
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.support_contact == request.user
