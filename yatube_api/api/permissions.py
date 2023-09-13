
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """При изменении или удалении проверяем, что изменяет или удаляет автор.
    При получении проверяем что пользователь аутентифицирован."""

    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )
