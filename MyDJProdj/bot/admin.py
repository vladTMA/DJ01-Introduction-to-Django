# bot\admin.py
from django.contrib import admin
from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    # Какие поля показывать в списке
    list_display = (
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "language_code",
        "is_subscribed",
        "last_activity",
        "registered_at",
    )

    # По каким полям можно искать
    search_fields = (
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "language_code",
    )

    # Фильтры справа
    list_filter = (
        "language_code",
        "is_subscribed",
    )

    # Поля только для чтения
    readonly_fields = (
        "registered_at",
        "last_activity",
        "created_at",
    )

    # Сортировка по умолчанию
    ordering = ("-last_activity",)

    # Группировка полей в карточке пользователя
    fieldsets = (
        ("Основная информация", {
            "fields": (
                "telegram_id",
                "username",
                "first_name",
                "last_name",
                "language_code",
            )
        }),
        ("Активность", {
            "fields": (
                "registered_at",
                "last_activity",
                "is_subscribed",
            )
        }),
        ("Геолокация", {
            "fields": (
                "latitude",
                "longitude",
            ),
            "classes": ("collapse",)
        }),
        ("Служебные данные", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )

    list_per_page = 30
