# main/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('neo/', views.neo, name="neo"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts"),
    path("articles/", views.articles, name="articles"),
    path("articles/<int:pk>/", views.article_detail, name="article_detail"),
]


