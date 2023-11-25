from rest_framework import permissions,status
from rest_framework.exceptions import APIException

class CustomForbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "你還未登入"


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.auth:
            raise CustomForbidden
