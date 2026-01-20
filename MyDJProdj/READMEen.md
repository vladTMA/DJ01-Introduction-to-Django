# 🇬🇧 English README Version

---

# MyDJProdj — Django Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)


A training Django project created while learning the framework.  
Includes a news system, NEO code‑viewer page, navigation, templates, and admin customization.

---

## 📸 Screenshots
| Home | News | Books | Neo |
|------|------|-------|-----|
| ![](MyDJProdj/screenshots/homedj.png) | ![](MyDJProdj/screenshots/news.png) | ![](MyDJProdj/screenshots/books.png) | ![](MyDJProdj/screenshots/neo.png) |


---

## 🚀 Features

### Main pages
- `/` — Home
- `/neo/` — Code viewer (Prism.js + dark theme)
- `/about/` — About
- `/contacts/` — Contacts

### News
- `/news/` — All news
- `/news/<id>/` — News detail
- Bootstrap cards
- “Read more”
- Auto‑assigned author

### Books
- `/books/` — list of books
- `/books/<id>/` — detailed book page
- Covers, description, reviews
- Cards with a "Learn more" button

### Admin panel
- Custom card layout
- Search, filters, sorting
- Slug display
- Collapsible service fields

---

## 📂 Project structure

```text
MyDJProdj/
│
├── main/
│   ├── migrations/
│   ├── static/
│   │   └── main/
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── main/
│   │       ├── about.html
│   │       ├── add_book.html
│   │       ├── article_delete_confirm.html
│   │       ├── article_form.html
│   │       ├── article_list.html
│   │       ├── article_preview.html
│   │       ├── articles.html
│   │       ├── book_detail.html
│   │       ├── book_list.html
│   │       ├── contacts.html
│   │       ├── index.html
│   │       └── neo.html
│   │
│   ├── blocks/
│   │   ├── detail.html
│   │   ├── footer.html
│   │   ├── header.html
│   │   └── list.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── news/
│   ├── migrations/
│   ├── admin/
│   │   └── news/
│   │       └── change_list.html
│   │
│   ├── templates/
│   │   └── news/
│   │       ├── detail.html
│   │       ├── home.html
│   │       └── news.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── books/
│
├── screenshots/
│   ├── homedj.png
│   ├── news.png
│   ├── books.png
│   └── neo.png
│
├── .env
├── env.example
├── requirements.txt
├── run_django.bat
├── stop_django.bat
├── manage.py
└── venv/

```
---

### ▶️ Running the project

## 1. Using the script

run_django.bat

## 2. Manually

cd MyDJProdj
venv\Scripts\activate
python manage.py runserver

---

### ⏹ Stopping the server

stop_django.bat

---

### 🛠 Technologies

Python 3.11
Django 5.2
Bootstrap 5
Prism.js
HTML + CSS

---

### 📌 Roadmap

- Pagination
- News categories
- Images for news
- Contact form

---

### 📄 License                                

Educational use only.

---



