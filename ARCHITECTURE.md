# 📁 Project Architecture — MyDJProdj

Полная структура проекта с кастомной админкой, пользовательской регистрацией, модулями контента и расширенной логикой.

## 🧱 Дерево каталогов (сокращённо)

```text
DJ01-Introduction-to-Django/          ← корень репозитория (git)
│
├── ARCHITECTURE.md
├── CHANGELOG.md
├── LICENSE
├── README.md
│
└── MyDJProdj/                        ← рабочая папка Django-проекта (manage.py)
    │
    ├── MyDJProdj/                    ← пакет конфигурации (settings, urls, wsgi, asgi)
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── settings_local.py         ← опциональные локальные переопределения
    │   ├── urls.py                   ← корневой URLconf: admin, main, news, api
    │   └── wsgi.py
    │
    ├── main/                         ← основное приложение: страницы, статьи, книги, neo
    │   ├── management/commands/
    │   │   └── backupdb.py           ← кастомная команда бэкапа БД
    │   ├── migrations/
    │   ├── static/main/
    │   │   └── style.css
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── login.html
    │   │   ├── register.html
    │   │   └── main/                 ← шаблоны приложения main
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    │
    ├── bot/                          ← REST API для Telegram-бота
    │   ├── migrations/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py                 ← TelegramUser и др.
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── news/
    │   ├── migrations/
    │   ├── templates/
    │   │   ├── home.html
    │   │   ├── admin/news/news/change_list.html
    │   │   └── news/
    │   │       ├── detail.html
    │   │       ├── home.html
    │   │       └── news.html
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── weather/                      ← погода (OpenWeatherMap, шаблон с картой)
    │   ├── migrations/
    │   ├── templates/weather/
    │   │   └── weather.html
    │   ├── context_processors.py     ← данные для подвала (footer)
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    │
    ├── templates/admin/
    │   └── index.html                ← переопределение главной страницы админки
    │
    ├── backups/                      ← файлы *.sqlite3 от backupdb (в git могут не попадать)
    ├── media/books/                  ← загрузки обложек книг
    ├── screenshots/                  ← скриншоты для README
    │
    ├── .env                          ← секреты (локально; часто в .gitignore)
    ├── .env.example / EnvExample     ← шаблон переменных для копирования в .env
    ├── bot_main.py                   ← точка входа Telegram-бота (отдельный процесс)
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── READMEru.md
    ├── READMEen.md
    ├── run_all.bat
    └── stop_all.bat
```

## 💬 Комментарии к ключевым файлам

| Путь | Назначение |
|------|------------|
| **`MyDJProdj/manage.py`** | Стандартная точка входа Django: `runserver`, `migrate`, `shell` и т.д. |
| **`MyDJProdj/MyDJProdj/settings.py`** | Глобальные настройки: `INSTALLED_APPS`, БД, `load_dotenv()`, ключи API (`WEATHER_API_KEY`), `REST_FRAMEWORK`, CORS. |
| **`MyDJProdj/MyDJProdj/urls.py`** | Корневые маршруты: кастомная админка (`main.admin`), включение **`main.urls`**, префикс **`news/`**, API **`api/`** → `bot.urls`. Медиа в `DEBUG`. |
| **`MyDJProdj/main/urls.py`** | Публичные страницы: главная, регистрация/логин, статьи, книги, **`weather/`** (include `weather.urls`), **`neo/`**. |
| **`MyDJProdj/main/views.py`** | Представления главной части сайта, страница NEO (просмотр кода), статьи и книги. |
| **`MyDJProdj/main/models.py`** | Кастомный пользователь, статьи, книги и связанные модели. |
| **`MyDJProdj/main/admin.py`** | Регистрация моделей и **`BackupAdminSite`** (кастомная админка). |
| **`MyDJProdj/bot/urls.py`**, **`views.py`**, **`serializers.py`** | REST API бота: регистрация пользователя, профиль; защита через `X-BOT-SECRET`. |
| **`MyDJProdj/bot/models.py`** | Модель **`TelegramUser`** (telegram_id, подписка, геоданные и т.д.). |
| **`MyDJProdj/bot_main.py`** | Запуск aiogram/long polling; обращается к Django по HTTP, не через `manage.py`. |
| **`MyDJProdj/weather/views.py`** | Запросы к OpenWeatherMap, контекст для шаблона погоды и карты. |
| **`MyDJProdj/weather/context_processors.py`** | Краткие данные погоды для общего шаблона (например, подвал). |
| **`MyDJProdj/templates/admin/index.html`** | Кастомная разметка главной страницы админки. |
| **`MyDJProdj/main/management/commands/backupdb.py`** | Команда резервного копирования SQLite в **`backups/`**. |
| **`MyDJProdj/run_all.bat`** / **`stop_all.bat`** | Запуск Django (порт 8001) и бота в одном окне; остановка процессов по командной строке. Подробнее в **READMEru.md** / **READMEen.md**. |

---


