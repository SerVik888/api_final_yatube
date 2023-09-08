
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from posts.models import Follow


class IsOwnerOrReadOnly(permissions.BasePermission):
    """При изменении или удалении проверяем, что изменяет или удаляет автор.
    При получении проверяем что пользователь аутентифицирован."""

    def has_permission(self, request, view):
        if (
            request.method not in permissions.SAFE_METHODS
            and not request.user.is_authenticated
        ):
            return False
        return True

    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )


class SubscribePermissions(permissions.BasePermission):
    """При добавлении проверяем, что пользователь не подписывается на себя
    и что такой подписки нет."""

    def has_permission(self, request, view):
        follow = Follow.objects.filter(
            user_id=request.user.id,
            following__username=request.data.get('following')
        )
        if (
            request.method == 'POST'
            and follow
            or request.user.username == request.data.get('following')
        ):
            raise ValidationError(
                "Вы уже подписаны на этого пользоавтеля или"
                + "вы пытаетесь подписаться на самого себя."
            )
        return True
