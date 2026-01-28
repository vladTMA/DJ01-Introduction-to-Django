# weather/urls.py
from django.urls import path
from .views import weather_view, add_favorite_city, remove_favorite_city

urlpatterns = [
    path("", weather_view, name="weather"),
    path("add/", add_favorite_city, name="add_favorite_city"),
    path("remove/<str:city>/", remove_favorite_city, name="remove_favorite_city"),
]