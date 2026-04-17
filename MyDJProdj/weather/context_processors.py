# weather/context_processors.py
from .utils import get_weather

def footer_weather(request):
    weather = get_weather("Moscow")
    return {"footer_weather": weather}
