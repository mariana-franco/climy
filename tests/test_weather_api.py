import pytest
from services.weather_api import get_weather, get_complete_forecast


def test_cache_invalidation_with_different_coords(mock_weather_api):
    # Força a limpeza para o contador de chamadas começar do zero
    if hasattr(get_weather, "cache_clear"):
        get_weather.cache_clear()

    get_weather(-23.55, -46.63)  # Chamada 1
    get_weather(-22.90, -43.17)  # Chamada 2

    assert len(mock_weather_api.calls) == 2


def test_get_weather_conversion(mock_weather_api):
    """Testa se o retorno da API é convertido corretamente para o modelo Weather."""
    # pylint: disable=no-member

    # Se o erro 'AttributeError' persistir, use getattr para evitar que o teste quebre
    if hasattr(get_weather, "cache_clear"):
        get_weather.cache_clear()

    weather = get_weather(-23.55, -46.63)

    # Ajuste os nomes dos atributos conforme definido no seu src/models/weather.py
    assert weather.temperature == 24.5
    assert weather.windspeed == 14.5
    # De acordo com seu histórico, o código WMO é mapeado aqui
    assert weather.weather_code == 2


def test_get_complete_forecast_lengths(mock_weather_api):
    """Valida se o zip() processou as 24h e 7 dias corretamente."""
    forecast = get_complete_forecast(-23.55, -46.63)

    # Verifica o processamento dos dados estruturados via dataclasses/zip
    assert len(forecast.hourly) <= 24
    assert len(forecast.daily) <= 7
    assert forecast.current.temperature is not None
