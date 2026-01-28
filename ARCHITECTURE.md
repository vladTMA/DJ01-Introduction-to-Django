# 📁 Project Architecture — MyDJProdj

Полная структура проекта с кастомной админкой, пользовательской регистрацией, модулями контента и расширенной логикой.

## 🧱 Project Architecture

```text
MyDJProdj/
├── ARCHITECTURE.md
├── bot_main.py
├── LICENSE
└── README.md
    │
    ├── MyDJProdj/
    │   ├── backups/
    │   ├── migrations/    
    │   ├── bot/   
    │   ├── __init__.py                     
    │   ├── admin.py
    │   ├── apps.py                 
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py)                        
    │       
    ├── main/
    │   └── management/
    │           └── commands/
    │                 └── backupdb.py
    │   └── migrations/ 
    │   └── static/
    │           └── main/ 
    │                └── style.css
    │   └── templates/
    │            main/
    │               └── blocks/
    │                       ├── detail.html
    │                       ├── footer.html
    │                       ├── header.html
    │                       └── list.html
    │                 
    │              └── about.html    │                   
    │              ├── add_book.html
    │              ├── article_delete_confirm.html
    │              ├── article_detail.html
    │              ├── article_form.html
    │              ├── article_list.html
    │              ├── article_preview.html
    │              ├── articles.html
    │              ├── book_detail.html
    │              ├── book_list.html
    │              ├── contacts.html
    │              ├── index.html
    │              └── neo.html  
    │   ├── __init__.py 
    │   ├── admin.py              # кастомная админка (BackupAdminSite)
    │   ├── apps.py               # регистрация моделей в кастомной админке
    │   ├── forms.py              # кастомная регистрация пользователя
    │   ├── templates/
    │   │   ├── admin/            # переопределённые шаблоны админки
    │   │   └── registration/     # кастомная форма регистрации│   
    │   ├── models.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    │
    ├── media/
    │           └── books/
    │
    ├── MyDJProdj/
    │       ├── __init__.py                
    │       ├── asgi.py
    │       ├── settings.py                 
    │       ├── settings_local.py
    │       ├── urls.py
    │       └── wsgi.py)    │
    │ 
    ├── news/
    │     └── migrations/
    │     └── templates/
    │            └── admin 
    │                  └── news
    │                       └── news 
    │                            └── change_list.html 
    │               └── news/  
    │                     └── templates/ 
    │                     ├── detail.html
    │                     ├── home.html                     
    │                     └── news.html 
    │               └── home.html 
    │       ├── __init__.py
    │       ├── admin.py              # NewsAdmin без регистрации (регистрация в apps.py)
    │       ├── apps.py
    │       ├── models.py
    │       ├── tests.py
    │       ├── urls.py
    │       └── views.py
    
    │
    ├── screenshots/
    │      
    ├── templates/ 
    │       └── admin/
    │              └── index.htm 
    │               
    ├── venv/
    │
    ├── weather/
    │     └── migrations/
    │     └── static/
    │            └── weather/
    │                  └── icons/ 
    │     └── templates/
    │            └── weather 
    │                  └── weather.html    │               
    │      └──__init__.py
    │      ├── admin.py
    │      ├── apps.py     
    │      ├── context_processors.py
    │      ├── models.py
    │      ├── tests.py
    │      ├── urls.py
    │      ├── utils.py
    │      └── views.py   
    ├── .env
    ├── .env.example
    ├── db.sqlite3
    ├── manage.py
    ├── READMEru.md
    ├── READMEen.md
    ├── requirements.txt
    ├── run_all.bat
    └── stop_all.bat
```