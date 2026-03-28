import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def _int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


# --- Metadados ---
APP_NAME = "Climy"  # Alinhado com a interface
APP_VERSION = "1.0.0"

# --- Caminhos ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- APIs (Endpoints Fixos) ---
BASE_GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
BASE_WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# --- Timeouts e Cache ---
# Reduzi o timeout para 5s, 15s pode travar a UI do Streamlit por muito tempo
TIMEOUT = _int("CLIMY_TIMEOUT", 5)
CACHE_TTL = _int("CLIMY_CACHE_TTL", 300)

# --- Unidades ---
# Importante: O dashboard assume Celsius (°). Se mudar aqui, tem que tratar na UI.
TEMPERATURE_UNIT = "celsius"
WINDSPEED_UNIT = "kmh"

# --- Configurações de exibição (Usar no weather_api.py) ---
MAX_CITIES_RESULTS = _int("CLIMY_MAX_CITIES", 10)
FORECAST_DAYS = _int("CLIMY_FORECAST_DAYS", 7)
HOURLY_FORECAST_HOURS = _int("CLIMY_HOURLY_HOURS", 24)

# --- Idioma (Open-Meteo Geocoding suporta language) ---
API_LANGUAGE = os.getenv("CLIMY_LANGUAGE", "pt")
