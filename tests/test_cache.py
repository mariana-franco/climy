import pytest
from services.weather_api import get_weather
from services.weather_api import _get_weather_cached


def reset_my_cache():
    _get_weather_cached.cache_clear()


def test_cache_invalidation_with_different_coords(mock_weather_api):
    # Força a limpeza para o contador de chamadas começar do zero
    if hasattr(get_weather, "cache_clear"):
        get_weather.cache_clear()

    get_weather(-23.55, -46.63)  # Chamada 1
    get_weather(-22.90, -43.17)  # Chamada 2

    assert len(mock_weather_api.calls) == 2


def test_weather_cache_hits(mock_weather_api):
    # Agora get_weather tem esse atributo graças à nossa alteração acima
    get_weather.cache_clear()

    # Chamada 1: Deve ir para o Mock (calls = 1)
    get_weather(-23.55, -46.63)
    # Chamada 2: Deve vir do cache (calls continua 1)
    get_weather(-23.55, -46.63)

    assert len(mock_weather_api.calls) == 1
