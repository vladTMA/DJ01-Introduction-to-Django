# main/apps.py
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        from .admin import admin_site, ArticleAdmin, BookAdmin
        from .models import Article, Book
        admin_site.register(Article, ArticleAdmin)
        admin_site.register(Book, BookAdmin)

        # Регистрация News
        from news.models import News
        from news.admin import NewsAdmin
        admin_site.register(News, NewsAdmin)