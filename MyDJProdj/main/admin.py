# main/admin.py
from django.contrib import admin
from .models import Article, Book

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Основная информация", {
            "fields": ("title", "subtitle", "content")
        }),
        ("Публикация", {
            "fields": ("author", "is_published"),
            "classes": ("collapse",)  # сворачиваем блок
        }),
        ("Служебные данные", {
            "fields": ("slug", "created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    list_display = ("title", "slug", "author", "created_at", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "subtitle", "content")
    readonly_fields = ("slug",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')


