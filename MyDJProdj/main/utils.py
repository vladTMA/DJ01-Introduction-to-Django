# main/utils.py
from datetime import datetime
import pytz

moscow_tz = pytz.timezone("Europe/Moscow")

def to_moscow(ts):
    return datetime.fromtimestamp(ts, tz=moscow_tz).strftime("%d.%m.%Y %H:%M")
