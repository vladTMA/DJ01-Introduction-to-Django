# MyDJProdj — Django Project

Добро пожаловать в мой учебный Django‑проект.  
Здесь реализованы новости, книги, статьи, загрузка изображений, кастомная регистрация пользователей и полностью переработанная админ‑панель с расширенным функционалом.

## 🌐 Documentation / Документация

- 🇷🇺 **Русская версия** → [READMEru.md](MyDJProdj/READMEru.md)
- 🇬🇧 **English version** → [READMEen.md](MyDJProdj/READMEen.md)

---

## 📸 Screenshots
| Home | News | Books | Neo |
|------|------|-------|-----|
| ![](MyDJProdj/screenshots/homedj.png) | ![](MyDJProdj/screenshots/news.png) | ![](MyDJProdj/screenshots/books.png) | ![](MyDJProdj/screenshots/neo.png) |

### Custom registration & Adin panel
| Custom Registration                            | Custom Admin (Backup DB) |
|------------------------------------------------|--------------------------|
| ![](MyDJProdj/screenshots/castom_register.png) | ![](MyDJProdj/screenshots/custom_admin_backup.png) |

---

## 🧱 Project Structure

Полная структура проекта вынесена в отдельный файл:

➡️ [ARCHITECTURE.md](ARCHITECTURE.md)

---
## 🚀 Features

- Новости, книги, статьи
- Загрузка изображений
- Кастомная регистрация пользователя
- Кастомная админ‑панель (BackupAdminSite)
- Кнопка резервного копирования базы данных
- Блок статистики на главной странице админки
- Переопределённые шаблоны Django Admin
- Адаптивный интерфейс на Bootstrap
- Работа с .env
- Чистая и расширяемая архитектура проекта

---

## ⚙️ Installation

``` bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```
---

## 📄 License

MIT License

---
