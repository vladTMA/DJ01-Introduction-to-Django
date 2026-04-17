# bot/views.py
from django.conf import settings
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser
from .serializers import TelegramUserSerializer


def check_bot_secret(request):
    secret = request.headers.get("X-BOT-SECRET")
    return secret == settings.BOT_API_SECRET


@api_view(['POST'])
def register_user(request):

    # 🔐 Проверка секрета
    if not check_bot_secret(request):
        return Response({"error": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

    data = request.data

    user, created = TelegramUser.objects.get_or_create(
        telegram_id=data['telegram_id'],
        defaults={
            'username': data.get('username'),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'language_code': data.get('language_code'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
        }
    )

    # обновляем last_activity
    user.last_activity = timezone.now()
    user.save()

    serializer = TelegramUserSerializer(user)

    return Response({
        "status": "ok",
        "created": created,
        "user": serializer.data
    }, status=201 if created else 200)


@api_view(['GET'])
def get_user_info(request, telegram_id):
    # 🔐 Проверка секрета
    if not check_bot_secret(request):
        return Response({"error": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = TelegramUser.objects.get(telegram_id=telegram_id)
    except TelegramUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)

    serializer = TelegramUserSerializer(user)

    return Response({
        "status":
        "ok",
        "user": serializer.data
    })

