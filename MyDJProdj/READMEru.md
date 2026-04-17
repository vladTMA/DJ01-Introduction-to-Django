# MyDJProdj — учебный Django‑проект

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)

Учебный Django‑проект, включающий новости, книги, статьи, загрузку изображений, кастомную регистрацию пользователей, расширенную админ‑панель и полноценную интеграцию с Telegram‑ботом через REST API.

## 📸 Скриншоты

| Домашняя страница           | Новости                   | Книги                      | Программирование (Neo)   |
|-----------------------------|---------------------------|----------------------------|--------------------------|
| ![](screenshots/homedj.png) | ![](screenshots/news.png) | ![](screenshots/books.png) | ![](screenshots/neo.png) |

### Кастомная регистрация и админ-панель
| Кастомная регистрация                | Кастомная админ-панель |
|--------------------------------------|--------------------------|
| ![](screenshots/custom_register.png) | ![](screenshots/custom_admin_backup.png) |


| Погода (город)                     | Погода (результат поиска)              |
|-------------------------------------|----------------------------------------|
| ![](screenshots/weather_Alagir.png) | ![](screenshots/weather_Hong_Kong.png) |
                        
---

## 🚀 Функциональность

### Django

#### Основные страницы
- `/` — главная
- `/about/` — о проекте
- `/books/` — каталог книг
- `/contacts/` — контакты
- `/news/` — новости
- `/neo/` — страница с подсветкой кода (Prism.js + тёмная тема)
- `/register/` — кастомная регистрация
- `/weather/` — страница погоды (OpenWeatherMap API)

#### Админка
- Полностью кастомный BackupAdminSite
- Кнопка резервного копирования базы данных
- Блок статистики на главной странице
- Переопределённые шаблоны Django Admin
- Поиск, фильтры, сортировка
- Отображение slug
- Служебные поля в collapsible‑блоках

#### Новости
- `/news/` — список новостей
- `/news/<id>/` — детальная страница
- Bootstrap‑карточки
- «Читать далее»
- Автоматическое назначение автора

#### Книги
- `/books/` — список книг
- `/books/<id>/` — детальная страница книги
- Обложки, описание, отзыв
- Карточки с кнопкой «Подробнее» 

#### Пользователи
- Кастомная регистрация
- Кастомная форма
- Расширенная валидация

#### 🌤 Страница погоды

Модуль Погода (Weather) предоставляет:

- поиск погоды по названию города
- карту города
- отображение температуры, влажности, скорости ветра
- время восхода и захода солнца по местному и московскому времени, UTC
- продолжительность дня
- высоту города над уровнем моря
- Bootstrap‑карточки
- обработку ошибок API
- интеграцию с Telegram‑ботом

---
## 🤖 Интеграция Telegram‑бота и Django

Проект включает полноценную двустороннюю интеграцию Django и Telegram‑бота.

### 🔗 REST API для бота

Бот взаимодействует с Django через защищённый API:

- POST /api/v1/register/ — регистрация пользователя
- GET /api/v1/user/<telegram_id>/ — получение профиля

Все запросы защищены заголовком:

```
X-BOT-SECRET: <секретный ключ>
```
### 👤 Модель TelegramUser

Хранит:

- Telegram ID
- username, имя, фамилию
- язык пользователя
- дату регистрации
- последнюю активность
- статус подписки
- геолокацию

### Функции бота

- /start — регистрация и вывод профиля
- /myinfo — получение данных из Django
- /weather — погода в Пскове
- /погода <город> — погода в любом городе мира
- Авторассылка погоды в 08:00 и 20:00
- Inline‑кнопки:
  - «Погода в Пскове»
  - «Выбрать город»
  - «Помощь»
  - «Остановить авторассылку»

### 🧩 Единая архитектура

Django хранит данные

- бот — интерфейс взаимодействия с пользователем
- API — связующее звено
- админка — центр управления

### 🛡 Безопасность

- доступ к API только через секретный ключ
- сериализатор ограничивает доступные поля
- админ‑панель позволяет управлять пользователями бота

---

## 📡 API Reference

### POST /api/v1/register/

Регистрирует пользователя Telegram.

Схема запроса

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

Пример запроса

```
{
  "telegram_id": 123456,
  "username": "vivaldy",
  "first_name": "Ilia",
  "last_name": "Voronov",
  "language_code": "ru",
  "latitude": null,
  "longitude": null
  }
}
```

### GET /api/v1/user/<telegram_id>/

Возвращает профиль пользователя.

Пример ответа

```
{
  "status": "ok",
  "created": true,
  "user": {
    "telegram_id": 123456,
    "username": "vivaldy",
    "first_name": "Ilia",
    "last_name": "Voronov",
    "language_code": "ru",
    "registered_at": "...",
    "last_activity": "...",
    "is_subscribed": true
  }
}
```

---

## 📂 Структура проекта

Полная структура проекта вынесена в отдельный файл:

➡️ [ARCHITECTURE.md](../ARCHITECTURE.md)
---

--- 

## ⚙️ Installation / Инсталляция

``` bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001

```

### 🖥 Windows: `.bat` scripts / Скрипты `.bat`

✔ *run_all.bat* — единый запуск

- Django запускается на порту 8001
- Telegram‑бот работает в фоне
- Логи пишутся в:
```
logs/django.log
logs/bot.log
```
---

### 2. Запуск вручную

```
cd MyDJProdj
venv\Scripts\activate
python manage.py runserver 8001
```
---

## ⏹ Безопасная остановка + время работы процессов (stop_all.bat)

- останавливает Django по порту 8001
- останавливает бота по имени bot_main.py
- показывает uptime каждого процесса
- работает в UTF‑8 (stop_all.bat)

---

## 🛠 Используемые технологии

- Python 3.x  
- Django 5.2
- Bootstrap 5
- Prism.js (подсветка кода)                                
- HTML + CSS 

---

## 📌 Планы по развитию

- Пагинация новостей
- Категории
- Изображения к новостям
- Категории новостей
- Форма обратной связи
- Улучшение дизайна админки

---

## 📄 Лицензия

Лицензия: MIT

```
