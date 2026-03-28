import pytest
import responses
from tests.mocks.mock_data import MOCK_WEATHER_API_RESPONSE, MOCK_CITIES
from src.config import BASE_WEATHER_URL, BASE_GEOCODING_URL
from services.weather_api import get_weather


@pytest.fixture(autouse=True)
def reset_cache_per_test():
    """Limpa o cache antes de cada teste individual."""
    if hasattr(get_weather, "cache_clear"):
        get_weather.cache_clear()
    yield


@pytest.fixture
def mock_weather_api():
    """Fixture para simular a resposta da API de clima."""
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET, BASE_WEATHER_URL, json=MOCK_WEATHER_API_RESPONSE, status=200
        )
        yield rsps


@pytest.fixture
def mock_geo_api():
    """Fixture para simular a resposta da Geocoding API."""
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET, BASE_GEOCODING_URL, json={"results": MOCK_CITIES}, status=200
        )
        yield rsps
