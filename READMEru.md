# MyDJProdj — учебный Django‑проект

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)

Учебный проект, созданный в процессе изучения Django.  
Содержит систему новостей, страницу NEO с подсветкой кода, навигацию, шаблоны и кастомизацию админки.

---

## 📸 Скриншоты
| Home | News | Books | Detail                          |
|------|------|-------|---------------------------------|
| ![](static/screenshots/homedj.png) | ![](static/screenshots/news.png) | ![](static/screenshots/books.png) | ![](static/screenshots/nto.png) |
                          

---

## 🚀 Функциональность

### Основные страницы
- `/` — главная
- `/neo/` — страница с подсветкой кода (Prism.js + тёмная тема)
- `/about/` — о проекте
- `/contacts/` — контакты

### Новости
- `/news/` — список новостей
- `/news/<id>/` — детальная страница
- Bootstrap‑карточки
- «Читать далее»
- Автоматическое назначение автора

### Админка
- Карточки новостей
- Поиск, фильтры, сортировка
- Отображение slug
- Служебные поля в collapsible‑блоках

---

## 📂 Структура проекта

```text
MyDJProdj/
│
├── main/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── neo.html
│   │   ├── about.html
│   │   └── contacts.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── news/
│   ├── templates/news/
│   │   ├── home.html
│   │   ├── detail.html
│   │   └── ...
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── run_django.bat
├── stop_django.bat
├── manage.py
└── venv/

---

## ▶️ Запуск проекта

### 1. Через скрипт

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

Скрипт:

- определяет процессы Django
- завершает их
- показывает статус
- работает в кодировке UTF‑8

---
---

## 🛠 Используемые технологии

- Python 3.x  
- Django 5.2
- Bootstrap 5
- Prism.js  (подсветка кода)                                
- HTML + CSS 

---

## 📌 Планы по развитию

- Пагинация новостей
- Категории
- Изображения к новостям
- Добавить категории новостей
- Сделать форму обратной связи
- Улучшить дизайн админки

---

## 📄 Лицензия

Проект создан в учебных целях.

```