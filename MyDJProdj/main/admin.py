# main/admin.py
from django.contrib import admin, messages
from django.core.management import call_command
from django.db.models import Count
from django.contrib.auth import get_user_model
from news.models import News
from django.shortcuts import redirect
from django.urls import path
from .models import Article, Book


# 1. Определяем кастомную админку
class BackupAdminSite(admin.AdminSite):
    site_header = "Администрирование проекта"
    site_title = "Админка"
    index_title = "Добро пожаловать"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("backup-db/", self.admin_view(self.backup_db), name="backup-db"),
        ]
        return custom_urls + urls

    def backup_db(self, request):
        try:
            call_command("backupdb")
            messages.success(request, "База данных успешно сохранена!")
        except Exception as e:
            messages.error(request, f"Ошибка: {e}")

        return redirect("admin:index")

    def each_context(self, request):
        context = super().each_context(request)

        User = get_user_model()
        context.update({
            "stats": {
                "articles": Article.objects.count(),
                "books": Book.objects.count(),
                "news": News.objects.count(),
                "users": User.objects.count(),
            }
        })

        return context

# 2. Создаём экземпляр кастомной админки
admin_site = BackupAdminSite(name="backup_admin")


# 3. Регистрируем модели
class ArticleAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Основная информация", {
            "fields": ("title", "subtitle", "content")
        }),
        ("Публикация", {
            "fields": ("author", "is_published"),
            "classes": ("collapse",)
        }),
    )

    list_display = ("title", "slug", "author", "created_at", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "subtitle", "content")
    readonly_fields = ("slug",)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')



