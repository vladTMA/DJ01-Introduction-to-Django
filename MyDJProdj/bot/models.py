# bot/models.py
from django.db import models

# Create your models here.
class TelegramUser(models.Model):

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"
        ordering = ["-last_activity"]

    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Добавляем поля для пользователя: язык, дата регистрации,
    # последнее действие, статус подписки и геолокация.
    language_code = models.CharField(max_length=10, null=True,
                                     blank=True)  # язык пользователя
    registered_at = models.DateTimeField(auto_now_add=True) # дата регистрации
    last_activity = models.DateTimeField(auto_now=True) # последнее действие
    is_subscribed = models.BooleanField(default=True) # статус подписки
    latitude = models.FloatField(null=True, blank=True) # широта
    longitude = models.FloatField(null=True, blank=True) # долгота

    def __str__(self):
        return f"{self.username or 'NoName'} ({self.telegram_id})"
