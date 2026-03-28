"""Serviço de integração com APIs do Open-Meteo."""

import logging
import math
from datetime import datetime
from functools import lru_cache
from typing import Any

import requests

from src.config import BASE_GEOCODING_URL, BASE_WEATHER_URL, TIMEOUT
from src.models.weather import DailyForecast, Weather, WeatherForecast

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configurações e Constantes
# ---------------------------------------------------------------------------

_VALID_FEATURE_CODES: frozenset[str] = frozenset(
    {
        "PPL",
        "PPLA",
        "PPLA2",
        "PPLA3",
        "PPLA4",
        "PPLC",
        "PPLF",
        "PPLG",
        "PPLL",
        "PPLR",
        "PPLS",
        "PPLW",
        "PPLX",
    }
)

_INVALID_FEATURE_CODES: frozenset[str] = frozenset(
    {
        "ADM1",
        "ADM2",
        "ADM3",
        "ADM4",
        "ADMD",
        "PCL",
        "PCLI",
        "PCLIX",
        "PCLF",
        "PCLD",
        "CONT",
        "RGN",
        "RGNE",
        "RGNL",
        "REG",
        "TERR",
        "ZN",
        "ZNB",
    }
)

_FEATURE_CODE_WEIGHT: dict[str, int] = {
    "PPLC": 100,
    "PPLA": 80,
    "PPLA2": 60,
    "PPLA3": 40,
    "PPLA4": 30,
    "PPL": 20,
    "PPLG": 20,
    "PPLL": 10,
    "PPLX": 5,
    "PPLF": 5,
    "PPLR": 5,
    "PPLW": 1,
    "PPLS": 1,
}

_MIN_NAME_LENGTH = 2
_MIN_SCORE = 10
_MAX_RESULTS = 5
_MIN_POPULATION = 100


class WeatherAPIError(Exception):
    """Erro na comunicação com a API de clima."""


# ---------------------------------------------------------------------------
# Lógica de Geocodificação e Scoring
# ---------------------------------------------------------------------------


def _score_city(result: dict[str, Any], query: str) -> int:
    score = 0
    feature_code = result.get("feature_code", "")
    score += _FEATURE_CODE_WEIGHT.get(feature_code, 0)

    population = result.get("population") or 0
    if population > 0:
        score += int(math.log10(population) * 8)

    name: str = result.get("name", "").lower()
    q = query.strip().lower()

    if name == q:
        score += 40
    elif name.startswith(q):
        score += 20
    elif q in name:
        score += 10

    if not result.get("country"):
        score -= 30
    if not result.get("admin1"):
        score -= 10
    if not result.get("latitude") or not result.get("longitude"):
        score -= 100

    return score


def search_cities(city: str, max_results: int = _MAX_RESULTS) -> list[dict[str, Any]]:
    if not city or not city.strip():
        return []

    query = city.strip()
    try:
        response = requests.get(
            BASE_GEOCODING_URL,
            params={"name": query, "count": 20, "language": "pt", "format": "json"},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError) as exc:
        raise WeatherAPIError(f"Erro na geocodificação: {exc}")

    raw_results = data.get("results", [])
    if not raw_results:
        return []

    scored = []
    for r in raw_results:
        f_code = r.get("feature_code", "")

        if f_code in _INVALID_FEATURE_CODES or f_code not in _VALID_FEATURE_CODES:
            continue
        if len(r.get("name", "")) < _MIN_NAME_LENGTH:
            continue
        if r.get("latitude") is None or r.get("longitude") is None:
            continue
        if (r.get("population") or 0) < _MIN_POPULATION:
            continue

        score = _score_city(r, query)
        if score >= _MIN_SCORE:
            scored.append((score, r))

    scored.sort(key=lambda x: (-x[0], x[1].get("name", "")))

    return [
        {
            "name": r.get("name", ""),
            "country": r.get("country", ""),
            "country_code": r.get("country_code", ""),
            "state": r.get("admin1", ""),
            "admin2": r.get("admin2", ""),
            "lat": r["latitude"],
            "lon": r["longitude"],
            "feature_code": r.get("feature_code", ""),
            "population": r.get("population") or 0,
            "elevation": r.get("elevation") or 0,
            "timezone": r.get("timezone", "UTC"),
        }
        for _, r in scored[:max_results]
    ]


# ---------------------------------------------------------------------------
# Clima e Previsão (com Cache e Zip)
# ---------------------------------------------------------------------------


def _ttl_bucket(seconds: int = 300) -> int:
    """Cria um identificador de tempo que muda a cada X segundos."""
    return int(datetime.now().timestamp() // seconds)


@lru_cache(maxsize=128)
def _get_weather_cached(lat: float, lon: float, _bucket: int) -> Weather:
    """Esta é a função que realmente detém o cache do lru_cache."""
    return _get_weather_core(lat, lon)


def get_weather(lat: float, lon: float, cache_ttl: int = 300) -> Weather:
    """Função pública. O Streamlit e os testes chamam ESTA aqui."""
    _validate_coordinates(lat, lon)
    bucket = _ttl_bucket(cache_ttl)
    return _get_weather_cached(lat, lon, bucket)


get_weather.cache_clear = _get_weather_cached.cache_clear


def _get_weather_core(lat: float, lon: float) -> Weather:
    """Lógica bruta de request (antiga _get_weather)."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,windspeed_10m,winddirection_10m,relative_humidity_2m,weather_code",
        "timezone": "auto",
    }

    data = _request_weather_api(params)

    try:
        current = data["current"]
        return Weather(
            temperature=current["temperature_2m"],
            windspeed=current["windspeed_10m"],
            winddirection=current["winddirection_10m"],
            time=current["time"],
            humidity=current.get("relative_humidity_2m"),
            pressure=None,
            weather_code=current.get("weather_code") or current.get("weathercode"),
        )
    except KeyError as exc:
        raise WeatherAPIError(f"Campo ausente na resposta: {exc}")


def get_rain_forecast(lat: float, lon: float, hours: int = 6) -> int | None:
    _validate_coordinates(lat, lon)
    hours = max(1, min(hours, 24))
    try:
        data = _request_weather_api(
            {
                "latitude": lat,
                "longitude": lon,
                "hourly": "precipitation_probability",
                "forecast_days": 1,
                "timezone": "auto",
            }
        )
        probs = data.get("hourly", {}).get("precipitation_probability", [])
        return max(probs[:hours]) if probs else None
    except WeatherAPIError:
        return None


def get_complete_forecast(lat: float, lon: float) -> WeatherForecast:
    _validate_coordinates(lat, lon)
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation_probability,weathercode",
        "daily": "weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset",
        "timezone": "auto",
        "forecast_days": 7,
    }
    data = _request_weather_api(params)
    current_raw = data.get("current_weather")
    if not current_raw:
        raise WeatherAPIError("Campo 'current_weather' ausente.")

    return WeatherForecast(
        current=Weather(
            temperature=current_raw["temperature"],
            windspeed=current_raw["windspeed"],
            winddirection=current_raw["winddirection"],
            time=current_raw["time"],
            weather_code=current_raw.get("weathercode"),
        ),
        hourly=_parse_hourly(data.get("hourly", {})),
        daily=_parse_daily(data.get("daily", {})),
    )


def _parse_hourly(hourly: dict[str, Any]) -> list[dict[str, Any]]:
    # Uso do zip para iterar de forma segura sobre múltiplas listas
    times = hourly.get("time", [])
    temps = hourly.get("temperature_2m", [])
    hums = hourly.get("relative_humidity_2m", [])
    rains = hourly.get("precipitation_probability", [])
    codes = hourly.get("weather_code", hourly.get("weathercode", []))

    if not times or not temps:
        logger.warning("Dados horários incompletos na resposta da API.")
        return []

    return [
        {
            "time": t,
            "temperature": temp,
            "humidity": hum,
            "rain_probability": rain,
            "weather_code": code,
        }
        for t, temp, hum, rain, code in zip(times, temps, hums, rains, codes)
    ][:24]


def _parse_daily(daily: dict[str, Any]) -> list[DailyForecast]:
    w_code = daily.get("weather_code", daily.get("weathercode", []))

    times = daily.get("time", [])
    t_max = daily.get("temperature_2m_max", [])
    t_min = daily.get("temperature_2m_min", [])
    sunrise = daily.get("sunrise", [])
    sunset = daily.get("sunset", [])

    if not times or not t_max:
        return []

    return [
        DailyForecast(
            date=d, max_temp=mx, min_temp=mn, sunrise=sr, sunset=ss, weather_code=wc
        )
        for d, mx, mn, sr, ss, wc in zip(times, t_max, t_min, sunrise, sunset, w_code)
    ][:7]


# ---------------------------------------------------------------------------
# Helpers e Validação
# ---------------------------------------------------------------------------


def validate_city(city_name: str) -> tuple[bool, str]:
    if not city_name or not city_name.strip():
        return False, "Informe o nome de uma cidade."
    try:
        cities = search_cities(city_name)
        if not cities:
            return False, f"'{city_name}' não encontrada."

        best = cities[0]
        loc = ", ".join(filter(None, [best.get("state"), best.get("country")]))
        pop = (
            f" · {best['population']:,} hab.".replace(",", ".")
            if best["population"]
            else ""
        )
        return True, f"Cidade encontrada: {best['name']} ({loc}){pop}"
    except WeatherAPIError:
        return False, "Erro ao validar cidade."


def _validate_coordinates(lat: float, lon: float) -> None:
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise ValueError(f"Coordenadas inválidas: lat={lat}, lon={lon}")


def _request_weather_api(params: dict[str, Any]) -> dict[str, Any]:
    try:
        response = requests.get(BASE_WEATHER_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as exc:
        raise WeatherAPIError(f"Erro de conexão com API: {exc}")
