# MyDJProdj — учебный Django‑проект

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)

Учебный проект, созданный в процессе изучения Django.  
Содержит систему новостей, каталог книг, страницу NEO с подсветкой кода, кастомную регистрацию пользователей и полностью переработанную админ‑панель с расширенным функционалом.

---

## 📸 Скриншоты

| Home | News | Books | Neo |
|------|------|-------|-----|
| ![](screenshots/homedj.png) | ![](screenshots/news.png) | ![](screenshots/books.png) | ![](screenshots/neo.png) |

### Custom registration & Adin panel
| Custom Registration | Custom Admin (Backup DB) |
|---------------------|--------------------------|
| ![](MyDJProdj/screenshots/custom_register.png) | ![](MyDJProdj/screenshots/custom_admin_backup.png) |
                        

---

## 🚀 Функциональность

### Основные страницы
- `/` — главная
- `/about/` — о проекте
- `/books/` — книги
- `/contacts/` — контакты
- `/news/` — новости
- `/neo/` — страница с подсветкой кода (Prism.js + тёмная тема)
- `/register/` — кастомная регистрация

### Админка
- Полностью кастомный BackupAdminSite
- Кнопка резервного копирования базы данных
- Блок статистики на главной странице
- Переопределённые шаблоны
- Кастомизированный список новостей
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

---

## 📂 Структура проекта

Полная структура проекта вынесена в отдельный файл:

➡️ [ARCHITECTURE.md](ARCHITECTURE.md)
---

## ▶️ Запуск проекта

### 1. Через скрипт

Если используете встроенный скрипт:

```
run_django.bat
```
Скрипт автоматически:

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

Скрипт:

- находит процессы Django
- завершает их
- выводит статус
- работает в кодировке UTF‑8

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