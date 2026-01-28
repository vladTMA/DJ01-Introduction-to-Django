# main/admin.py

from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.core.management import call_command
from django.shortcuts import redirect
from django.urls import path

from .models import Article, Book
from news.models import News
from bot.models import TelegramUser


# ============================================================
# 1. Кастомная админка
# ============================================================

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


# Экземпляр кастомной админки
admin_site = BackupAdminSite(name="backup_admin")


# ============================================================
# 2. Админ-классы
# ============================================================

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
    ordering = ("-created_at",)
    list_per_page = 20
    date_hierarchy = "created_at"


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author")
    ordering = ("-created_at",)
    list_per_page = 20


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("telegram_id", "username", "first_name", "last_activity", "is_subscribed")
    search_fields = ("telegram_id", "username", "first_name", "last_name")
    list_filter = ("language_code", "is_subscribed")
    readonly_fields = ("registered_at", "last_activity")
    ordering = ("-last_activity",)
    list_per_page = 30


# ============================================================
# 3. Регистрация моделей
# ============================================================

User = get_user_model()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)

admin_site.register(Article, ArticleAdmin)
admin_site.register(Book, BookAdmin)
admin_site.register(News)
admin_site.register(TelegramUser, TelegramUserAdmin)
