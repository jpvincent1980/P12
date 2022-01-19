import logging

from rest_framework.permissions import BasePermission, SAFE_METHODS


logger = logging.getLogger(__name__)


class IsSalesContact(BasePermission):
    """
    Custom permission to allow sales contact to update their client,
    client's contract and client's event data
    """
    def has_permission(self, request, view):
        return request.user.department == "SALES"

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
        return request.user.department == "SUPPORT"

    def has_object_permission(self, request, view, obj):
        return obj.support_contact == request.user
