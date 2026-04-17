![Banner](https://img.shields.io/badge/MyDJProdj-Django%20%2B%20Telegram%20Bot-0C4B33?style=for-the-badge&logo=python&logoColor=white)

# MyDJProdj — Django Project / Django Проект 

Учебный Django‑проект, включающий новости, книги, статьи, загрузку изображений, кастомную регистрацию пользователей, расширенную админ‑панель и полноценную интеграцию с Telegram‑ботом через REST API.

Educational Django project featuring news, books, articles, image uploads, custom user registration, an extended admin panel, and full Telegram bot integration via REST API.

## 🌐 Documentation / Документация

- 🇷🇺 **Русская версия** → [READMEru.md](MyDJProdj/READMEru.md)
- 🇬🇧 **English version** → [READMEen.md](MyDJProdj/READMEen.md)

---

## 📸 Screenshots / Скриншрты
| Home | News | Books | Neo |
|------|------|-------|-----|
| ![](MyDJProdj/screenshots/homedj.png) | ![](MyDJProdj/screenshots/news.png) | ![](MyDJProdj/screenshots/books.png) | ![](MyDJProdj/screenshots/neo.png) |

### Custom registration & Adin panel / Кастомная регистрация и админ-панель
| Custom Registration                  | Custom Admin (Backup DB) |
|--------------------------------------|--------------------------|
| ![](MyDJProdj/screenshots/custom_register.png) | ![](MyDJProdj/screenshots/custom_admin_backup.png) |

## 🌤 Weather Page (Screenshots) / Погода (скриншоты)
| Weather (City Input)                | Weather (Result)                                 |
|-------------------------------------|--------------------------------------------------|
| ![](MyDJProdj/screenshots/weather_Alagir.png) | ![](MyDJProdj/screenshots/weather_Hong_Kong.png) |
---

## 🧱 Project Structure / Структура проекта
Полная структура проекта вынесена в отдельный файл:

➡️ [ARCHITECTURE.md](ARCHITECTURE.md)

---
## 🚀 Features / Функции

## Django

- Новости, книги, статьи
- Загрузка изображений
- Кастомная регистрация пользователя
- Кастомная админ‑панель (BackupAdminSite)
- Кнопка резервного копирования базы данных
- Блок статистики на главной странице админки
- Переопределённые шаблоны Django Admin
- Адаптивный интерфейс на Bootstrap
- Работа с .env
- Чистая и расширяемая архитектура проекта
- Страница погоды /weather/ (OpenWeatherMap API)

---

## Telegram Bot

- Автоматическая регистрация пользователя
- Команда /myinfo — получение профиля из Django
- Команда /weather — погода в Пскове
- Команда /погода <город> — погода по названию города
- Авторассылка погоды
- Inline‑кнопки и интерактивное меню
- Полная синхронизация данных с Django

---

## 🔗 REST API для бота

Бот взаимодействует с Django через защищённый API:
- POST /api/v1/register/ — регистрация пользователя
- GET /api/v1/user/<telegram_id>/ — получение профиля

Все запросы защищены заголовком: 

X-BOT-SECRET: <секретный ключ>

---

## 👤 Модель TelegramUser
Хранит:

-Telegram ID
 - username, имя, фамилию
- язык пользователя
- дату регистрации
- последнюю активность
- статус подписки
- геолокацию

---

## 🛡 Security / Безопасность

- доступ к API только через секретный ключ
- сериализатор ограничивает доступные поля
- админ‑панель позволяет управлять пользователями бота
- рекомендуется HTTPS в продакшене

--- 

## 🤖 Bot Features / Функции бота

- /start — регистрация и вывод профиля
- /myinfo — получение данных из Django
- /weather — погода в Пскове
- /погода <город> — погода по названию города
- авторассылка погоды
- inline‑кнопки

---

## 🧩 Unified Architecture / Единая архитектура

- Django хранит данные
- бот — интерфейс для пользователя
- API — связующее звено
- админка — центр управления

---

## 📡 API Reference
## POST /api/v1/register/

Регистрирует пользователя Telegram.

## Request (JSON)/ Схема запроса

```
{
  "telegram_id": <int>,
  "username": <string | null>,
  "first_name": <string>,
  "last_name": <string>,
  "language_code": <string>,
  "latitude": <float | null>,
  "longitude": <float | null>
}
```
---

## Example request/ Пример запроса

```
{
  "telegram_id": 123456,
  "username": "vivaldy",
  "first_name": "Vladimir",
  "last_name": "Filonoff",
  "language_code": "ru",
  "latitude": null,
  "longitude": null
}
```
## Example answer (text)/ Пример ответа
```
{
  "status": "ok",
  "created": true,
  "user": {
    "telegram_id": 123456,
    "username": "vivaldy",
    "first_name": "Vladimir",
    "last_name": "Filonoff",
    "language_code": "ru",
    "registered_at": "...",
    "last_activity": "...",
    "is_subscribed": true
  }
}
```
---

#### GET /api/v1/user/<telegram_id>/

Возвращает профиль пользователя.

## Example answer (text)/ Пример ответа

```
{
  "status": "ok",
  "created": true,
  "user": {
    "telegram_id": 123456,
    "username": "vivaldy",
    "first_name": "Vladimir",
    "last_name": "Filonoff",
    "language_code": "ru",
    "registered_at": "...",
    "last_activity": "...",
    "is_subscribed": true
  }
}
```
--- 

## ⚙️ Installation / Инсталляция

``` bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

### 🖥 Windows: `.bat` scripts / Скрипты `.bat`

✔ *run_all.bat* — единое окно + логи в файлы

- Django запускается на порту 8001
- Telegram‑бот запускается в фоне
- Логи пишутся в:

```
logs/django.log
logs/bot.log
```
---

## 📄 License / Лтцензия

MIT License

---
