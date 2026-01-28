# bot/serializers.py
from rest_framework import serializers
from .models import TelegramUser

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = [
            "telegram_id",
            "username",
            "first_name",
            "last_name",
            "language_code",
            "latitude",
            "longitude",
            "registered_at",
            "last_activity",
            "is_subscribed",
        ]
        read_only_fields = [
            "registered_at",
            "last_activity",
        ]
