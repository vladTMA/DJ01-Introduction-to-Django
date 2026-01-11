# MyDJProdj — учебный Django‑проект

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)


Учебный проект, созданный в процессе изучения Django.  
Содержит базовую структуру приложения, несколько страниц, навигационное меню и шаблоны с наследованием.

---

## 🚀 Функциональность

- Главная страница `/`
- Страница NEO `/neo/`
- Страница «О проекте» `/about/`
- Страница «Контакты» `/contacts/`
- Базовый шаблон `base.html` с навигацией
- Наследование шаблонов для всех страниц
- Удобные скрипты для запуска и остановки сервера

---

## 📂 Структура проекта

```
MyDJProdj/
│
├── main/                     # Основное приложение
│   ├── templates/            # HTML-шаблоны
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── neo.html
│   │   ├── about.html
│   │   └── contacts.html
│   ├── __init__.py
│   ├── admin.py
│   ├── views.py              # Логика страниц
│   ├── urls.py               # Маршруты приложения
│   └── ...
│
├── MyDJProdj/                # Настройки Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── venv/                     # Виртуальное окружение (локально)
```

---

## ▶️ Запуск проекта

### 1. Активировать виртуальное окружение

Если используете встроенный скрипт:

```
run_django.bat
```

Он автоматически:

- переходит в папку проекта  
- активирует виртуальное окружение  
- запускает сервер  

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
stop_django.bat
```

Он:

- определяет процессы Django
- завершает их
- показывает статус
- работает в кодировке UTF‑8

---

## 🌐 Доступные страницы

| URL            | Описание                |
|----------------|--------------------------|
| `/`            | Главная                 |
| `/neo/`        | Вторая страница         |
| `/about/`      | О проекте               |
| `/contacts/`   | Контакты                |

---

## 🛠 Используемые технологии

- Python 3.x  
- Django 5.2  
- HTML + CSS  
- Шаблоны Django (Template Inheritance)

---

## 📌 Планы по развитию

- Вынести CSS в `static/`
- Добавить Bootstrap
- Сделать активное меню
- Добавить формы (контакты, обратная связь)
- Подключить базу данных и модели

---

## 📄 Лицензия

Проект создан в учебных целях.
```