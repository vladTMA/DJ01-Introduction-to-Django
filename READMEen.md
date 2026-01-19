---

# 🇬🇧 English README Version

```markdown
# MyDJProdj — Django Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)

A training Django project created while learning the framework.  
Includes a news system, NEO code‑viewer page, navigation, templates, and admin customization.

---

## 📸 Screenshots

| Home | News | Books | Detail                          |
|------|------|-------|---------------------------------|
| ![](static/screenshots/homedj.png) | ![](static/screenshots/news.png) | ![](static/screenshots/books.png) | ![](static/screenshots/neo.png) |


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
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── news/
│   ├── templates/news/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── media/
│   └── books/
│
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



