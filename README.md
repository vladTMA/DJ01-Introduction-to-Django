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

### Основные страницы 
- Главная страница `/` 
- Страница NEO `/neo/` 
- Страница «О проекте» `/about/` 
- Страница «Контакты» `/contacts/` 
- 
### Новости 
- Страница всех новостей `/news/` 
- Страница новости (detail) `/news/<id>/` 
- Вывод последних новостей на главной 
- Карточки Bootstrap для новостей 
- Кнопка «Читать далее» 
- Автоматическое заполнение автора при создании новости 

### Админка 
- Кастомный вывод новостей в виде карточек 
- Кнопка удаления новости прямо в списке 
- Поиск, фильтры, сортировка 
- Автоматическое назначение автора

---

## 📂 Структура проекта

```
MyDJProdj/
│
├── main/                     # Основное приложение
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── neo.html
│   │   ├── about.html
│   │   └── contacts.html
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── news/                     # Приложение новостей
│   ├── templates/
│   │   └── news/
│   │       ├── home.html
│   │       ├── detail.html
│   │       └── ...
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├├── news/                     # Приложение новостей
│   ├── templates/
│   │   └── news/
│   │       ├── home.html
│   │       ├── detail.html
│   │       └── ...
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├── news/                     # Приложение новостей
│   ├── templates/
│   │   └── news/
│   │       ├── home.html
│   │       ├── detail.html
│   │       └── ...
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
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

Скрипт:

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
| `/news/`       | Все новости             |
| `/news/<id>/`  | Страница новости        |

---

## 🛠 Используемые технологии

- Python 3.x  
- Django 5.2  
- HTML + CSS 
- Bootstrap 5 
- Django Templates (наследование, блоки, контекст)

---

## 📌 Планы по развитию

- Вынести CSS в `static/`
- Добавить изображения к новостям
- Добавить slug‑URL для новостей
- Реализовать пагинацию
- Добавить категории новостей
- Сделать форму обратной связи
- Улучшить дизайн админки

---

## 📄 Лицензия

Проект создан в учебных целях.
```