# weather/views.py
import datetime
import pytz
import requests

from django.conf import settings
from django.shortcuts import render, redirect
from .utils import translate_description, get_day_length

# Create your views here.
def weather_view(request):
    city = request.GET.get("city")

    context = {}
    context["favorites"] = request.session.get("favorites", [])

    if city:
        api_key = settings.WEATHER_API_KEY
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}&units=metric&lang=ru"
        )
        data = requests.get(url).json()

        if data.get("cod") != 200:
            context["error"] = "Город не найден"
        else:
            sunrise_utc = datetime.datetime.fromtimestamp(
                data["sys"]["sunrise"], tz=datetime.timezone.utc
            )
            sunset_utc = datetime.datetime.fromtimestamp(
                data["sys"]["sunset"], tz=datetime.timezone.utc
            )

            # Москва
            moscow_tz = pytz.timezone("Europe/Moscow")
            sunrise_moscow = sunrise_utc.astimezone(moscow_tz)
            sunset_moscow = sunset_utc.astimezone(moscow_tz)

            # Локальное время города
            offset = data["timezone"] # секунды
            city_tz = datetime.timezone(datetime.timedelta(seconds=offset))

            sunrise_local = sunrise_utc.astimezone(city_tz)
            sunset_local = sunset_utc.astimezone(city_tz)

            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]

            lat_dir = "с.ш." if lat >= 0 else "ю.ш."
            lon_dir = "в.д." if lon >= 0 else "з.д."

            # Высота над уровнем моря
            elev_url = f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}"
            elev_data = requests.get(elev_url).json()

            elevation = None
            if "elevation" in elev_data and elev_data["elevation"]:
                elevation = elev_data["elevation"][0]

            context.update({
                "city": city,
                "temp": data["main"]["temp"],
                "temp_min": data["main"]["temp_min"],
                "temp_max": data["main"]["temp_max"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": translate_description(data["weather"][0]["description"]),
                "icon": data["weather"][0]["icon"],
                "sunrise_utc": sunrise_utc,
                "sunset_utc": sunset_utc,
                "sunrise_moscow": sunrise_moscow,
                "sunset_moscow": sunset_moscow,
                "sunrise_local": sunrise_local,
                "sunset_local": sunset_local,
                "day_length": get_day_length(sunrise_utc, sunset_utc),
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"],
                "context_lat": f"{abs(lat):.4f}° {lat_dir}",
                "context_lon": f"{abs(lon):.4f}° {lon_dir}",
                "elevation": elevation,
            })

    return render(request, "weather/weather.html", context)


def add_favorite_city(request):
    if request.method == "POST":
        city = request.POST.get("city")
        favorites = request.session.get("favorites", [])

        if city not in favorites:
            favorites.append(city)
            request.session["favorites"] = favorites

    return redirect("weather")


def remove_favorite_city(request, city):
    favorites = request.session.get("favorites", [])
    if city in favorites:
        favorites.remove(city)
        request.session["favorites"] = favorites

    return redirect("weather")




