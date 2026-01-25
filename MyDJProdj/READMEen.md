# 🇬🇧 English README Version

---

# MyDJProdj — Django Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-0C4B33?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-templates-orange?style=for-the-badge)
![CSS](https://img.shields.io/badge/CSS-basic-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)


A learning‑oriented Django project featuring a news system, book catalog, NEO code viewer, custom user registration, and a fully customized admin panel with extended functionality.

---

## 📸 Screenshots
| Home | News | Books | Neo |
|------|------|-------|-----|
| ![](screenshots/homedj.png) | ![](screenshots/news.png) | ![](screenshots/books.png) | ![](screenshots/neo.png) |

### Custom registration & Adin panel
| Custom Registration                            | Custom Admin (Backup DB) |
|------------------------------------------------|--------------------------|
| ![](screenshots/castom_register.png) | ![](screenshots/custom_admin_backup.png) |
---

## 🚀 Features

### Main pages
- `/` — Home
- `/about/` — About
- `/books/` —  List of books
- `/contacts/` — Contacts
- `/news/` — List of news
- `/neo/` — Code viewer (Prism.js + dark theme)
- `/register/` — Custom registration

### Admin panel
- Fully custom BackupAdminSite
- One‑click database backup
- Statistics block on the admin homepage
- Overridden Django admin templates
- Search, filters, sorting
- Collapsible service fields

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

### User system

- Custom user registration
- Custom form and validation
- Extended authentication flow

---

## 📂 Project structure

The full project structure is available in a separate file:

➡️ [ARCHITECTURE.md](../ARCHITECTURE.md)

---

### ▶️ Running the project

## 1. Using the script

```
run_django.bat
```
The script automatically:

- navigates to the project directory
- activates the virtual environment
- starts the development server

## 2. Running manually

```
cd MyDJProdj
venv\Scripts\activate
python manage.py runserver
```

---

### ⏹ Stopping the server

```
stop_django.bat
```
The script:

- finds Django processes
- terminates them
- prints status
- works in UTF‑8
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
- Improved admin UI

---

### 📄 License                                

MIT License
Educational use only.

---



