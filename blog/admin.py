from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'content', 'status')
    search_fields = ('title', 'excerpt', 'content',)
    list_filter = ('status', 'updated', 'created')

    actions = ['publish', 'un_publish']

    def publish(self, request, queryset):
        updated = queryset.update(status="published")
        self.message_user(request, ngettext(
            '%d Post has successfully published.',
            '%d Posts have been successfully published.',
            updated,
        ) % updated, messages.SUCCESS)

    publish.short_description = "publish post"

    def un_publish(self, request, queryset):
        updated = queryset.update(status="draft")
        self.message_user(request, ngettext(
            '%d Post has successfully unpublished.',
            '%d Posts have been successfully unpublished.',
            updated,
        ) % updated, messages.INFO)

    un_publish.short_description = "un publish post"

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True
