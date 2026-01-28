# MyDJProdj — учебный Django‑проект

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)

Учебный Django‑проект, включающий новости, книги, статьи, загрузку изображений, кастомную регистрацию пользователей, расширенную админ‑панель и полноценную интеграцию с Telegram‑ботом через REST API.

## 📸 Скриншоты

| Home | News | Books | Neo |
|------|------|-------|-----|
| ![](screenshots/homedj.png) | ![](screenshots/news.png) | ![](screenshots/books.png) | ![](screenshots/neo.png) |

### Кастомная регистрация и админ-панель
| Custom Registration                            | Custom Admin (Backup DB) |
|------------------------------------------------|--------------------------|
| ![](screenshots/castom_register.png) | ![](screenshots/custom_admin_backup.png) |
                        

---

## 🚀 Функциональность

### Основные страницы
- `/` — главная
- `/about/` — о проекте
- `/books/` — каталог книг
- `/contacts/` — контакты
- `/news/` — новости
- `/neo/` — страница с подсветкой кода (Prism.js + тёмная тема)
- `/register/` — кастомная регистрация
- `/weather/` — страница погоды (OpenWeatherMap API)

### Админка
- Полностью кастомный BackupAdminSite
- Кнопка резервного копирования базы данных
- Блок статистики на главной странице
- Переопределённые шаблоны Django Admin
- Поиск, фильтры, сортировка
- Отображение slug
- Служебные поля в collapsible‑блоках

### Новости
- `/news/` — список новостей
- `/news/<id>/` — детальная страница
- Bootstrap‑карточки
- «Читать далее»
- Автоматическое назначение автора

### Книги
- `/books/` — список книг
- `/books/<id>/` — детальная страница книги
- Обложки, описание, отзыв
- Карточки с кнопкой «Подробнее» 

### Пользователи
- Кастомная регистрация
- Кастомная форма
- Расширенная валидация

### 🌤 Страница погоды

Модуль Weather предоставляет:

- поиск погоды по названию города
- отображение температуры, влажности, ветра
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

- бот — интерфейс для пользователя
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

Пример запроса

```
{
  "telegram_id": 123456,
  "username": "vivaldy",
  "first_name": "Vladimir",
  "last_name": "Trofimov",
  "language_code": "ru",
  "latitude": null,
  "longitude": null
}
```

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

## ▶️ Запуск проекта

### 1. Через скрипт

Если используете встроенный скрипт:

```
run_all.bat
```
Скрипт автоматически:

- переходит в папку проекта  
- активирует виртуальное окружение  
- запускает сервер и телеграм бота


### 2. Запуск вручную

```
cd MyDJProdj
venv\Scripts\activate
python manage.py runserver
```

---

## ⏹ Остановка сервера

Используйте удобный скрипт:

```
stop_all.bat
```

Скрипт:

- находит процессы Django
- завершает их
- выводит статус
- работает в кодировке UTF‑8

Скрипты run_all.bat и stop_all.bat выведены на страницу neo

---
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

Проект создан в учебных целях.
MIT лицензия

```
