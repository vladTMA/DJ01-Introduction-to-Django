# main/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from .views import RegisterView, CustomLoginView


urlpatterns = [

    # Главная
    path('', views.index, name="index"),

    # Аутентификация
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),

    # Информационные страницы
    path('neo/', views.neo, name="neo"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts"),

    # Статьи
    path("articles/", views.articles, name="articles"),
    path("articles/add/", views.add_article, name="add_article"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path("articles/<slug:slug>/edit/", views.edit_article, name="edit_article"),
    path("articles/<slug:slug>/delete/", views.delete_article, name="delete_article"),

    # Книги
    path("books/add/", views.add_book, name="add_book"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),

    # Погода
    path("weather/", include("weather.urls")),

    # Админка
    path('admin/', admin.site.urls),

    # API Telegram‑бота
    path('api/v1/', include('bot.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
