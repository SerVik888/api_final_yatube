from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly, SubscribePermissions
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Comment, Follow, Group, Post, User


class FollowViewSet(viewsets.ModelViewSet):
    """Обрабатывает запрос на получение, создание, редактирование,
    удаления одной подписки и получинея списка подписок автора
    который отправил запрос.
    """

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, SubscribePermissions)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        """При создании подписки меняем поле в ответе с числа на имя автора
        или подпищика
        """
        serializer.save(
            user=self.request.user,
            following=get_object_or_404(
                User,
                username=self.request.data.get('following')
            )
        )

    def get_queryset(self):
        """Получаем подписки принадлежащий пользователю."""
        return get_object_or_404(User, id=self.request.user.id).users.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Обрабатывает запрос на получение, создание, редактирование,
    удаления одной группы и получинея списка групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    """Обрабатывает запрос на получение, создание, редактирование,
    удаления одного поста и получинея списка постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """При создании поста меняем поле в ответе с числа на имя автора"""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Обрабатывает запрос на получение, создание, редактирование,
    удаления одного комментария и получинея списка комментариев."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_post(self):
        """Получаем объект поста."""
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        """При создании комментария меняем поле автор в ответе с числа на имя
        автора и поле пост с числа на название поста.
        """
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )

    def get_queryset(self):
        """Получаем список комментариев принадлежащий данному посту."""
        return self.get_post().comments.all()
