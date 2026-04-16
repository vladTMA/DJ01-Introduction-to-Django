# bot_main.py
import os
import time
import math
import datetime
import threading
import requests
import telebot
from telebot import types
from dotenv import load_dotenv

# ==========================
# 🔧 Загрузка переменных окружения
# ==========================
load_dotenv(dotenv_path="MyDJProdj/.env")

BOT_SECRET = os.getenv("BOT_API_SECRET")
DJANGO_API = os.getenv("DJANGO_API_URL")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("WEATHER_API_KEY")

bot = telebot.TeleBot(TOKEN)
active_reminders = {}

# ==========================
# 🌤 Города
# ==========================
CITIES = {
    "Псков": "Pskov,RU",
    "Москва": "Moscow,RU",
    "Санкт-Петербург": "Sanct-Peterburg,RU",
    "Воронеж": "Voronezh,RU",
    "Калининград": "Kaliningrad,RU"
}

# ==========================
# 🔌 API-клиент Django
# ==========================
def register_user(user):
    url = f"{DJANGO_API}/register/"
    payload = {
        "telegram_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "language_code": user.language_code,
        "latitude": None,
        "longitude": None,
    }

    try:
        r = requests.post(
            url,
            json=payload,
            headers={"X-BOT-SECRET": BOT_SECRET},
            timeout=5
        )
        print("STATUS:", r.status_code)
        print("TEXT:", r.text)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_user_info(user_id):
    url = f"{DJANGO_API}/user/{user_id}/"
    try:
        r = requests.get(
            url,
            headers={"X-BOT-SECRET": BOT_SECRET},
            timeout=5
        )
        return r.json()
    except Exception as e:
        return {"error": str(e)}

# ==========================
# 🌤 Погода
# ==========================
def get_weather(city_query="Pskov,RU"):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city_query,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]['description']
        return f"🌤️ Погода в {city_query.split(',')[0]}: {temp}°C, {desc}"

    except Exception as e:
        return f"⚠️ Не удалось получить погоду: {e}"


def get_weather_by_name(city_name):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city_name,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]['description']
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Точка росы (формула Магнуса)
        a, b = 17.62, 243.12
        alpha = math.log(humidity / 100) + (a * temp) / (b + temp)
        dew_point = round((b * alpha) / (a - alpha), 1)

        return (
            f"🌤️ Погода в {city_name}:\n"
            f"Температура: {temp}°C\n"
            f"Описание: {desc}\n"
            f"💧 Влажность: {humidity}%\n"
            f"🌬 Скорость ветра: {wind_speed} м/с\n"
            f"❄️ Точка росы: {dew_point}°C"
        )

    except Exception as e:
        return f"⚠️ Не удалось получить погоду для '{city_name}': {e}"

# ==========================
# 🤖 Команды бота
# ==========================
@bot.message_handler(commands=["start"])
def start_message(message):
    chat_id = message.chat.id

    # Регистрация пользователя
    result = register_user(message.from_user)

    if "error" in result:
        bot.send_message(chat_id, f"⚠️ Ошибка регистрации: {result['error']}")

    user = result.get("user", {})
    created = result.get("created", False)

    if created:
        status_text = "🎉 Добро пожаловать! Вы успешно зарегистрированы."
    else:
        status_text = "🔄 Вы уже были зарегистрированы ранее."

    text = (
        f"{status_text}\n\n" 
        f"🧾 *Ваши данные:*\n" 
        f"ID: {user.get('telegram_id')}\n" 
        f"Имя: {user.get('first_name') or '—'}\n" 
        f"Фамилия: {user.get('last_name') or '—'}\n" 
        f"Username: @{user.get('username') or '—'}\n" 
        f"Язык: {user.get('language_code') or '—'}\n" 
        f"Дата регистрации: {user.get('registered_at') or '—'}\n" 
        f"Последняя активность: {user.get('last_activity') or '—'}"
    )

    bot.send_message(chat_id, text, parse_mode="Markdown")

    # Клавиатура
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🌤 Погода в Пскове", callback_data="weather"))
    keyboard.add(types.InlineKeyboardButton("📍 Выбрать город", callback_data="choose_city"))
    keyboard.add(types.InlineKeyboardButton("ℹ️ Помощь", callback_data="help"))
    keyboard.add(types.InlineKeyboardButton("⛔ Остановить", callback_data="stop"))

    bot.send_message(
        chat_id,
        "Привет! Хотите узнать погоду? Выберите действие:",
        reply_markup=keyboard
    )

    threading.Thread(target=weather_scheduler, args=(chat_id,), daemon=True).start()


@bot.message_handler(commands=['myinfo'])
def myinfo_handler(message):
    chat_id = message.chat.id
    telegram_id = message.from_user.id

    try:
        response = requests.get(
            f"{DJANGO_API}/user/{telegram_id}/",
            headers={"X-BOT-SECRET": BOT_SECRET},
            timeout=5
        )
    except Exception:
        bot.send_message(chat_id, "⚠️ Ошибка соединения с сервером.")
        return

    if response.status_code != 200:
        bot.send_message(chat_id, "⚠️ Профиль не найден. Попробуйте /start.")
        return

    resp = response.json()
    user = resp.get("user", {})

    text = (
        "📄 *Ваш профиль*\n\n"
        f"👤 Имя: {user.get('first_name') or '—'}\n"
        f"🔗 Username: @{user.get('username') or '—'}\n"
        f"🌐 Язык: {user.get('language_code') or '—'}\n"
        f"📅 Зарегистрирован: {user.get('registered_at') or '—'}\n"
        f"🕒 Последняя активность: {user.get('last_activity') or '—'}\n"
        f"📍 Широта: {user.get('latitude') or '—'}\n"
        f"📍 Долгота: {user.get('longitude') or '—'}"
    )

    bot.send_message(chat_id, text, parse_mode="Markdown")


@bot.message_handler(commands=["help"])
def help_message(message):
    help_text = (
        "📌 /help — получить меню\n"
        "📌 /weather — погода в Пскове\n"
        "📌 /погода <город> — узнать погоду в любом городе мира\n"
        "📌 /stop — остановить авторассылку"
    )
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=["погода"])
def handle_weather(message):
    parts = message.text.split(maxsplit=1)
    city_name = parts[1].strip() if len(parts) > 1 else "Псков"
    weather = get_weather_by_name(city_name)
    bot.send_message(message.chat.id, weather)


@bot.message_handler(commands=["weather"])
def weather_command(message):
    weather = get_weather()
    bot.send_message(message.chat.id, weather)

# ==========================
# 🔘 Callback-кнопки
# ==========================
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id

    if call.data == "help":
        help_message(call.message)

    elif call.data == "weather":
        bot.send_message(chat_id, get_weather())

    elif call.data == "choose_city":
        bot.send_message(chat_id, "Введите название города:")
        bot.register_next_step_handler(call.message, handle_city_input)

    elif call.data == "stop":
        active_reminders[chat_id] = False
        bot.send_message(chat_id, "⛔ Авторассылка остановлена.")

# ==========================
# 🏙 Ввод города
# ==========================
def handle_city_input(message):
    city_name = message.text.strip()
    weather = get_weather_by_name(city_name)
    bot.send_message(message.chat.id, weather)

# ==========================
# ⏰ Авторассылка погоды
# ==========================
def weather_scheduler(chat_id):
    weather_times = ["08:00", "20:00"]
    sent_today = set()

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time == "00:00":
            sent_today.clear()

        if current_time in weather_times and current_time not in sent_today:
            if active_reminders.get(chat_id, True):
                bot.send_message(chat_id, get_weather())
                sent_today.add(current_time)
                time.sleep(61)

        time.sleep(1)

# ==========================
# 🚀 Запуск бота
# ==========================
if __name__ == "__main__":
    bot.infinity_polling(
        timeout=10,
        long_polling_timeout=5,
    )
