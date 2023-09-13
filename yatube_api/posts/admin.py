from django.contrib import admin
from django.utils.html import format_html

from posts.models import Comment, Follow, Group, Post

admin.site.empty_value_display = 'Не задано'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Класс для настройки интерфейса админ-зоны модели Post."""

    NUM_OF_WORDS_OF_TEXT = 10

    list_display = (
        'get_short_text',
        'pub_date',
        'group',
        'get_comment_count',
        'image_tag',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('group',)

    @admin.display(description='Описание')
    def get_short_text(self, obj):
        """Получаем начальные слова текста описания поста."""
        return f'{" ".join(obj.text.split()[:self.NUM_OF_WORDS_OF_TEXT])} ...'

    @admin.display(description='Комментарии')
    def get_comment_count(self, obj):
        """Получаем колличество комментариев в посте."""
        return obj.comments.count()

    @admin.display(description='Изображение')
    def image_tag(self, obj):
        """Получаем картинку к посту."""
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" />'.format(obj.image.url)
            )
        return 'Не найдено'


admin.site.register(Group)
admin.site.register(Follow)
admin.site.register(Comment)
