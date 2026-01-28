# weather/utils.py
import requests                        


def translate_description(desc):
    translations = {
        "clear sky": "ясно",
        "few clouds": "малооблачно",
        "scattered clouds": "рассеянные облака",
        "broken clouds": "облачно с прояснениями",
        "shower rain": "ливень",
        "rain": "дождь",
        "thunderstorm": "гроза",
        "snow": "снег",
        "mist": "туман",
    }
    return translations.get(desc.lower(), desc)

def get_day_length(sunrise, sunset):
    delta = sunset - sunrise
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"


def get_weather(city):
    api_key = "..."
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    data = requests.get(url).json()

    if data.get("cod") != 200:
        return None

    return {
        "temp": data["main"]["temp"],
        "icon": data["weather"][0]["icon"],
        "desc": translate_description(data["weather"][0]["description"]),
    }

